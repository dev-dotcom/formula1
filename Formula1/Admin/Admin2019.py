from Formula1 import app, conn
from flask import render_template,request, flash, session, url_for
from werkzeug.utils import redirect

@app.route('/admin/Drivers2019')
def Index19():
    if 'loggedin' in session:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Drivers2019 ORDER BY Points DESC")
        data = cur.fetchall()
        cur.close()

        return render_template('/Admin/admin_D19.html', drivers2019=data)
    return redirect (url_for('login'))

@app.route('/admin/Drivers2019/insert', methods = ['POST', 'GET'])
def insert19():
    if 'loggedin' in session:
        if request.method == "POST":

            name = request.form['name']
            podiums = request.form['podiums']
            wins = request.form['wins']
            points = request.form['points']
            team = request.form['team']
            country = request.form['country']
            pp = request.form['pp']
            fl = request.form['fl']

            if name == "" or podiums=="" or wins=="" or points=="" or team=="" or country=="" or pp=="" or fl=="":
                flash(f"Could not submit. Check if you have provided any empty values.")
                return redirect('/admin/Drivers2019')
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO Drivers2019 (Driver_name,Podiums,Wins,Points,Team,Country,Pole_Positions,Fastest_Laps) VALUES (?,?,?,?,?,?,?,?)", (name,podiums,wins,points,team,country,pp,fl))
                cur = conn.cursor()
                flash("Data Inserted Successfully")
                return redirect('/admin/Drivers2019')
            except:        
                flash(f"{name} is already present. ")
                return redirect('/admin/Drivers2019')   
    return redirect (url_for('login'))

@app.route('/admin/Drivers2019/delete/<string:id_data>', methods = ['POST','GET'])
def delete19(id_data):
    if 'loggedin' in session:
        flash("Record Has Been Deleted Successfully")
        cur = conn.cursor()
        cur.execute("DELETE FROM Drivers2019 WHERE Driver_name=?", (id_data,))
        cur = conn.cursor()
        return redirect('/admin/Drivers2019')

    return redirect (url_for('login'))

@app.route('/admin/Drivers2019/update', methods= ['POST', 'GET'])
def update19():
    if 'loggedin' in session:
        if request.method == 'POST':
            id_data = request.form['id']
            name = request.form['name']
            podiums = request.form['podiums']
            wins = request.form['wins']
            points = request.form['points']
            team = request.form['team']
            country = request.form['country']
            pp = request.form['pp']
            fl = request.form['fl']

            if name == "" or podiums=="" or wins=="" or points=="" or team=="" or country=="" or pp=="" or fl=="":
                flash(f"Could not submit. Check if you have provided any empty values.")
                return redirect('/admin/Drivers2019')

            try:
                cur = conn.cursor()
                cur.execute("""
                UPDATE Drivers2019 SET Driver_name=?, Podiums=?, Wins=?, Points=?, Team=?, Country=?, Pole_Positions=?,Fastest_Laps=?
                WHERE Driver_name=?
                """, (name, podiums, wins,points,team,country,pp,fl,id_data))
                cur = conn.cursor()
                flash("Data Updated Successfully")
                return redirect('/admin/Drivers2019')
            except:
                flash(f"You cannot provide other driver name. {name} is already present in table")
                return redirect('/admin/Drivers2019')

    return redirect (url_for('login'))

@app.route('/admin/Constructors2019')
def IndexC19():
    if 'loggedin' in session:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Constructors2019 ORDER BY Points DESC")
        data = cur.fetchall()
        cur.close()

        return render_template('/Admin/admin_C19.html', constructors2019=data)
    return redirect (url_for('login'))

@app.route('/admin/Constructors2019/insert', methods = ['POST', 'GET'])
def insertC19():
    if 'loggedin' in session:
        if request.method == "POST":

            team = request.form['team']
            podiums = request.form['podiums']
            wins = request.form['wins']
            points = request.form['points']
            pp = request.form['pp']
            fl = request.form['fl']

            if team=="" or podiums=="" or wins=="" or points=="" or pp=="" or fl=="":
                flash(f"Could not submit. Check if you have provided any empty values.")
                return redirect('/admin/Constructors2019')
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO Constructors2019 (Team,Points,Podiums,Wins,Pole_Positions,Fastest_Laps) VALUES (?,?,?,?,?,?)", (team,points,podiums,wins,pp,fl))
                cur = conn.cursor()
                flash("Data Inserted Successfully")
                return redirect('/admin/Constructors2019')
            except:
                flash(f"{team} is already present.")
                return redirect('/admin/Constructors2019')

    return redirect (url_for('login'))

@app.route('/admin/Constructors2019/delete/<string:id_data>', methods = ['POST','GET'])
def deleteC19(id_data):
    if 'loggedin' in session:
        flash("Record Has Been Deleted Successfully")
        cur = conn.cursor()
        cur.execute("DELETE FROM Constructors2019 WHERE Team=?",(id_data,))
        conn.commit()
        return redirect('/admin/Constructors2019')
    return redirect (url_for('login'))

@app.route('/admin/Constructors2019/update', methods= ['POST', 'GET'])
def updateC19():
    if 'loggedin' in session:
        if request.method == 'POST':
            id_data = request.form['id']
            team = request.form['team']
            podiums = request.form['podiums']
            wins = request.form['wins']
            points = request.form['points']
            pp = request.form['pp']
            fl = request.form['fl']

            if team=="" or podiums=="" or wins=="" or points=="" or pp=="" or fl=="":
                flash(f"Could not submit. Check if you have provided any empty values.")
                return redirect('/admin/Constructors2019')
            try:
                cur = conn.cursor()
                cur.execute("""
                UPDATE Constructors2019 SET Team=?, Points=?, Podiums=?, Wins=?,Pole_Positions=?,Fastest_Laps=?
                WHERE Team=?
                """, (team,points,podiums,wins,pp,fl,id_data))
                conn.commit()
                flash("Data Updated Successfully")
                return redirect('/admin/Constructors2019')
            except:
                flash(f"You cannot provide other team name. {team} is already present.")
                return redirect('/admin/Constructors2019')
    return redirect (url_for('login'))
