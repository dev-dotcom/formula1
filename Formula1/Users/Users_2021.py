from Formula1 import app, conn
from flask import render_template


@app.route('/Drivers/Drivers2021')
def Drivers2021():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Drivers2021 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Drivers/Drivers2021.html', drivers2021=data)

@app.route('/Constructors/Constructors2021')
def Constructors2021():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Constructors2021 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    return render_template('Constructors/Constructors2021.html', constructors2021=data)


#