from Formula1 import app, conn
from flask import render_template

@app.route('/Drivers/Drivers2022')
def Drivers2022():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Drivers2022 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Drivers/Drivers2022.html', drivers2022=data)

@app.route('/Constructors/Constructors2022')
def Constructors2022():

    cur = conn.cursor()
    cur.execute("SELECT * FROM Constructors2022 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Constructors/Constructors2022.html', constructors2022=data)



