from Formula1 import app, conn
from flask import render_template,request, flash, session, url_for
from werkzeug.utils import redirect

@app.route('/admin/accounts')
def accounts():
    if 'loggedin' in session:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        cur.close()
        return render_template('/Admin/user_accounts.html', users=data)
    
    return redirect(url_for('login'))

@app.route('/admin/accounts/delete/<string:id_data>', methods = ['POST','GET'])
def delete(id_data):
    if 'loggedin' in session:
        flash("Record Has Been Deleted Successfully")
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE username=?",(id_data,))
        conn.commit()
        return redirect('/admin/accounts')
    return redirect (url_for('login'))