from Formula1 import app, conn
from flask import render_template

@app.route('/Drivers/Drivers2019')
def Drivers2019():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Drivers2019 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Drivers/Drivers2019.html', drivers2019=data)

@app.route('/Constructors/Constructors2019')
def Constructors2019():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Constructors2019 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Constructors/Constructors2019.html', constructors2019=data)


#