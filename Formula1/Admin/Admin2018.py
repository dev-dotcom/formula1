from Formula1 import app, conn
from flask import render_template,request, flash, session, url_for
from werkzeug.utils import redirect


@app.route('/admin/Drivers2018')
def Index18():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        cur = conn.cursor()
        cur.execute("SELECT * FROM Drivers2018 ORDER BY Points DESC")
        data = cur.fetchall()
        cur.close()
        return render_template('/Admin/admin_D18.html', drivers2018=data)
    
    return redirect(url_for('login'))

@app.route('/admin/Drivers2018/insert', methods = ['POST', 'GET'])
def insert18():
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
            cur = conn.cursor()

            if name == "" or podiums=="" or wins=="" or points=="" or team=="" or country=="" or pp=="" or fl=="":
                    flash(f"Could not submit. Check if you have provided any empty values.")
                    return redirect('/admin/Drivers2018')
            try:
                cur.execute("INSERT INTO Drivers2018 (Driver_name,Podiums,Wins,Points,Team,Country,Pole_Positions,Fastest_Laps) VALUES (?,?,?,?,?,?,?,?)", (name,podiums,wins,points,team,country,pp,fl))
                conn.commit()
                flash("Data Inserted Successfully")
                return redirect('/admin/Drivers2018')
            except:              
                flash(f"{name} is already present. ")
                return redirect('/admin/Drivers2018')

    return redirect(url_for('login'))

@app.route('/admin/Drivers2018/delete/<string:id_data>', methods = ['POST','GET'])
def delete18(id_data):
    if 'loggedin' in session:
        flash("Record Has Been Deleted Successfully")
        cur = conn.cursor()
        cur.execute("DELETE FROM Drivers2018 WHERE Driver_name=?", (id_data,))
        conn.commit()
        return redirect('/admin/Drivers2018')
    
    return redirect(url_for('login'))

@app.route('/admin/Drivers2018/update', methods= ['POST', 'GET'])
def update18():
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
                return redirect('/admin/Drivers2018')

            try:
                cur = conn.cursor()
                cur.execute("""
                UPDATE Drivers2018 SET Driver_name=?, Podiums=?, Wins=?, Points=?, Team=?, Country=?, Pole_Positions=?,Fastest_Laps=?
                WHERE Driver_name=?
                """, (name, podiums, wins,points,team,country,pp,fl,id_data))
                conn.commit()
                flash("Data Updated Successfully")
                return redirect('/admin/Drivers2018')

            except:
                flash(f"You cannot provide other driver name. {name} is already present in table")
                return redirect('/admin/Drivers2018')

    return redirect(url_for('login'))

@app.route('/admin/Constructors2018')
def IndexC18():
    if 'loggedin' in session:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Constructors2018 ORDER BY Points DESC")
        data = cur.fetchall()
        cur.close()
        return render_template('/Admin/admin_C18.html', constructors2018=data)
    return redirect (url_for('login'))

@app.route('/admin/Constructors2018/insert', methods = ['POST', 'GET'])
def insertC18():
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
                return redirect('/admin/Constructors2018')
            # try:
            cur = conn.cursor()
            cur.execute("INSERT INTO Constructors2018 (Team,Points,Podiums,Wins,Pole_Positions,Fastest_Laps) VALUES (?,?,?,?,?,?)", (team,points,podiums,wins,pp,fl))
            conn.commit()
            flash("Data Inserted Successfully")
            return redirect('/admin/Constructors2018')
            # except:
            #     flash(f"{team} is already present.")
            #     return redirect('/admin/Constructors2018')


    return redirect (url_for('login'))

@app.route('/admin/Constructors2018/delete/<string:id_data>', methods = ['POST','GET'])
def deleteC18(id_data):
    if 'loggedin' in session:
        flash("Record Has Been Deleted Successfully")
        cur = conn.cursor()
        cur.execute("DELETE FROM Constructors2018 WHERE Team=?",(id_data,))
        conn.commit()
        return redirect('/admin/Constructors2018')
    return redirect (url_for('login'))

@app.route('/admin/Constructors2018/update', methods= ['POST', 'GET'])
def updateC18():
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
                return redirect('/admin/Constructors2018')

            try:
                cur = conn.cursor()
                cur.execute("""
                UPDATE Constructors2018 SET Team=?, Points=?, Podiums=?, Wins=?,Pole_Positions=?,Fastest_Laps=?
                WHERE Team=?
                """, (team,points,podiums,wins,pp,fl,id_data))
                conn.commit()
                flash("Data Updated Successfully")
                return redirect('/admin/Constructors2018')
            except:
                flash(f"You cannot provide other team name. {team} is already present.")
                return redirect('/admin/Constructors2018')
    return redirect (url_for('login'))
