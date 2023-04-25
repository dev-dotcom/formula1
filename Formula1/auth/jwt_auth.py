from flask import request, jsonify, make_response
from Formula1 import app,conn
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
    
        if 'jwt-access-token' in request.headers:
            token = request.headers['jwt-access-token']
            
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            
            cur = conn.cursor()
            
            cur.execute("SELECT * FROM users WHERE username = ?", (data['username'],))
            
            result = cur.fetchone()
            cur.close()
            if result is not None:
                current_user = {'username': result[0], 'password': result[1], 'email' : result[2]}
            else:
                raise Exception('User not found')
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 403
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)

    return decorated

@app.route('/api/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (current_user['username'],))
    users = cur.fetchone()
    
    user_data = {
        'username': users[0],
        'password': users[1],
        'email': users[2]
    }
    
    cur.close()
    return jsonify({'users': user_data})

@app.route('/api/signin', methods=['POST'])
def jwt_login():

    auth = request.form

    if not auth or not auth.get('username') or not auth.get('password'):
        return make_response(
            'Could not verify. Please fill the form correctly.',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username = ?',(auth.get('username'),))
    user = cur.fetchone()
    cur.close()

    if not user:
        
        return make_response(
            'User does not exist. Please try again.',
            401
        )

    if check_password_hash(user[1], auth.get('password')):
        token = jwt.encode({
            'username': str(user[0]),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        app.logger.debug("User logged in - %s",user[0])
        return make_response(jsonify({'token': token.encode().decode('UTF-8')}), 201)
        
    
    return make_response(
        'Wrong Password. Please try again',
        403
    )
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.form
    username, email = data.get('username'), data.get('email')
    password = data.get('password')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    app.logger.debug("101 executed")
    user = cur.fetchone()
    if not user:
        app.logger.debug("Inside if")
        cur = conn.cursor()
        app.logger.debug("again cursor created")
        cur.execute("""INSERT INTO users(username,password,email) VALUES(?, ?, ?)""",
                    (username,generate_password_hash(password),email))
        app.logger.debug("data inserted successfully")
        conn.commit()
        cur.close()
  
        return make_response('Successfully registered.', 201)
    else:

        return make_response('User already exists. Please Log in.', 202)

#