from Formula1 import app, conn
from flask import render_template


@app.route('/Drivers/Drivers2020')
def Drivers2020():
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM Drivers2020 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Drivers/Drivers2020.html', drivers2020=data)

@app.route('/Constructors/Constructors2020')
def Constructors2020():

    cur = conn.cursor()
    cur.execute("SELECT * FROM Constructors2020 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Constructors/Constructors2020.html', constructors2020=data)

