from Formula1 import app, mysql
from flask import render_template,request, flash, session, url_for
from werkzeug.utils import redirect

@app.route('/admin/Drivers2021')
def Index21():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Drivers2021 ORDER BY Points DESC")
        data = cur.fetchall()
        cur.close()

        return render_template('/Admin/admin_D21.html', drivers2021=data)

    return redirect (url_for('login'))

@app.route('/admin/Drivers2021/insert', methods = ['POST', 'GET'])
def insert21():
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
                return redirect('/admin/Drivers2021')
            try:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO Drivers2021 (Driver_name,Podiums,Wins,Points,Team,Country,Pole_Positions,Fastest_Laps) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (name,podiums,wins,points,team,country,pp,fl))
                mysql.connection.commit()
                flash("Data Inserted Successfully")
                return redirect('/admin/Drivers2021')
            except:
                flash(f"{name} is already present. ")
                return redirect('/admin/Drivers2021')
    
    return redirect (url_for('login'))

@app.route('/admin/Drivers2021/delete/<string:id_data>', methods = ['POST','GET'])
def delete21(id_data):
    if 'loggedin' in session:
        flash("Record Has Been Deleted Successfully")
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Drivers2021 WHERE Driver_name=%s", (id_data,))
        mysql.connection.commit()
        return redirect('/admin/Drivers2021')

    return redirect (url_for('login'))

@app.route('/admin/Drivers2021/update', methods= ['POST', 'GET'])
def update21():
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
                return redirect('/admin/Drivers2021')
            try:
                cur = mysql.connection.cursor()
                cur.execute("""
                UPDATE Drivers2021 SET Driver_name=%s, Podiums=%s, Wins=%s, Points=%s, Team=%s, Country=%s, Pole_Positions=%s,Fastest_Laps=%s
                WHERE Driver_name=%s
                """, (name, podiums, wins,points,team,country,pp,fl,id_data))
                mysql.connection.commit()
                flash("Data Updated Successfully")
                return redirect('/admin/Drivers2021')
            except:
                flash(f"You cannot provide other driver name. {name} is already present in table")
                return redirect('/admin/Drivers2021')
    
    return redirect (url_for('login'))

@app.route('/admin/Constructors2021')
def IndexC21():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Constructors2021 ORDER BY Points DESC")
        data = cur.fetchall()
        cur.close()
        return render_template('/Admin/admin_C21.html', constructors2021=data)
    return redirect (url_for('login'))

@app.route('/admin/Constructors2021/insert', methods = ['POST', 'GET'])
def insertC21():
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
                return redirect('/admin/Constructors2021')
            try:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO Constructors2021 (Team,Points,Podiums,Wins,Pole_Positions,Fastest_Laps) VALUES (%s, %s, %s, %s, %s, %s)", (team,points,podiums,wins,pp,fl))
                mysql.connection.commit()
                flash("Data Inserted Successfully")
                return redirect('/admin/Constructors2021')
            except:
                flash(f"{team} is already present.")
                return redirect('/admin/Constructors2021')
    return redirect (url_for('login'))

@app.route('/admin/Constructors2021/delete/<string:id_data>', methods = ['POST','GET'])
def deleteC21(id_data):
    if 'loggedin' in session:
        flash("Record Has Been Deleted Successfully")
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Constructors2021 WHERE Team=%s",(id_data,))
        mysql.connection.commit()
        return redirect('/admin/Constructors2021')
    return redirect (url_for('login'))

@app.route('/admin/Constructors2021/update', methods= ['POST', 'GET'])
def updateC21():
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
                return redirect('/admin/Constructors2021')
            try:
                cur = mysql.connection.cursor()
                cur.execute("""
                UPDATE Constructors2021 SET Team=%s, Points=%s, Podiums=%s, Wins=%s,Pole_Positions=%s,Fastest_Laps=%s
                WHERE Team=%s
                """, (team,points,podiums,wins,pp,fl,id_data))
                mysql.connection.commit()
                flash("Data Updated Successfully")
                return redirect('/admin/Constructors2021')
            except:
                flash(f"You cannot provide other team name. {team} is already present.")
                return redirect('/admin/Constructors2021')
    return redirect (url_for('login'))
