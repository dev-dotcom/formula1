import re
from Formula1 import app, conn
from flask import render_template,request,session, url_for
from werkzeug.utils import redirect

@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        cur = conn.cursor()
        cur.execute('SELECT * FROM accounts WHERE username = ? AND password = ?', (username, password,))
        account = cur.fetchone()
        
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            app.logger.debug("Admin logged in - User: %s Password: %s",account[1],account[2])
            return redirect('/admin')
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html',msg=msg)

@app.route('/login/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   app.logger.debug("Admin logged out")
   return redirect('/')


@app.route('/login/profile')
def profile():
    if 'loggedin' in session:
        cur = conn.cursor()
        cur.execute('SELECT * FROM accounts WHERE id = ?', (session['id'],))
        account = cur.fetchone()
        return render_template('profile.html', account=account)
    return redirect(url_for('login'))

#