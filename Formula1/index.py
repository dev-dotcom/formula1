from Formula1 import app
from flask import render_template,session, url_for
from werkzeug.utils import redirect

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_index():
    if 'loggedin' in session:
        return render_template('/Admin/admin_index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/api')
def api():
    return render_template('api.html')

@app.route('/about')
def about():
    return render_template('about.html')