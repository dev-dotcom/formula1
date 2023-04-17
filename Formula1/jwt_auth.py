from flask import request, jsonify, make_response
from Formula1 import app,mysql
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'jwt-access-token' in request.headers:
            token = request.headers['jwt-access-token']
            
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            
            cursor = mysql.connection.cursor()
            
            cursor.execute("SELECT * FROM users WHERE username = %s", (data['username'],))
            
            result = cursor.fetchone()
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

@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (current_user['username'],))
    users = cursor.fetchone()
    
    user_data = {
        'username': users[0],
        'password': users[1],
        'email': users[2]
    }
    
    cursor.close()
    return jsonify({'users': user_data})

@app.route('/signin', methods=['POST'])
def jwt_login():
    # creates dictionary of form data
    auth = request.form

    if not auth or not auth.get('username') or not auth.get('password'):
        return make_response(
            'Could not verify. Please fill the form correctly.',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s',(auth.get('username'),))
    user = cursor.fetchone()
    cursor.close()

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
@app.route('/signup', methods=['POST'])
def signup():
    data = request.form
    username, email = data.get('username'), data.get('email')
    password = data.get('password')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if not user:

        cur.execute("INSERT INTO users(username,password,email) VALUES(%s, %s, %s)",
                    (username,generate_password_hash(password),email))
        mysql.connection.commit()
        cur.close()
  
        return make_response('Successfully registered.', 201)
    else:

        return make_response('User already exists. Please Log in.', 202)