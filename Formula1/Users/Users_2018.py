from Formula1 import app, mysql
from flask import render_template

@app.route('/Drivers/Drivers2018')
def Drivers2018():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Drivers2018 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Drivers/Drivers2018.html', drivers2018=data)

@app.route('/Constructors/Constructors2018')
def Constructors2018():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Constructors2018 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Constructors/Constructors2018.html', constructors2018=data)


