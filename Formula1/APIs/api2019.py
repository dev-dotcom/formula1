from Formula1 import app, conn
from flask import jsonify
from Formula1.auth.jwt_auth import token_required

@app.route('/api/Drivers2019')
@token_required
def get_Drivers2019(current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Drivers2019 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    drivers = []
    for row in data:
        drivers.append({
            "Name" : row[0],
            "Podiums" : row[1],
            "Wins" : row[2],
            "Points" : row[3],
            "Team" : row[4],
            "Country" : row[5],
            "Pole Positions" : row[6],
            "Fastest Laps" : row[7]
        })
    
    return jsonify({'Drivers2019' : drivers})

@app.route('/api/Drivers2019/<string:name>')
@token_required
def get_specificDrivers19(name,current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Drivers2019 WHERE Driver_name=?",(name,))
        data = cur.fetchall()
        cur.close()
        driver = {
            "Name" : data[0][0],
            "Podiums" : data[0][1],
            "Wins" : data[0][2],
            "Points" : data[0][3],
            "Team" : data[0][4],
            "Country" : data[0][5],
            "Pole Positions" : data[0][6],
            "Fastest Laps" : data[0][7]
        }
        return jsonify(driver)
    except:
        error = {
            'message' : 'Resource do not exists in database.'
        }
        return jsonify({'error' : error})

@app.route('/api/Constructors2019')
@token_required
def get_all_Cons_19(current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Constructors2019 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.close()

    team = []
    for row in data:
        team.append({
            "Team" : row[0],
            "Points" : row[1],
            "Podiums" : row[2],
            "Wins" : row[3],
            "Pole Positions" : row[4],
            "Fastest Laps" : row[5]
        })
    return jsonify({'constructors2019' : team})

@app.route('/api/Constructors2019/<string:name>')
@token_required
def get_specific_team19(name,current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    try:
        name = name.upper()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Constructors2019 WHERE Team=?",(name,))
        data = cur.fetchall()
        cur.close()

        team = {
            "Team" : data[0][0],
            "Points" : data[0][1],
            "Podiums" : data[0][2],
            "Wins" : data[0][3],
            "Pole Positions" : data[0][4],
            "Fastest Laps" : data[0][5]
        }
        return jsonify(team)
    except:
        error = {
            'message' : 'Resource do not exists in database.'
        }
        return jsonify({'error' : error})

@app.route('/api/Podiums2019')
@token_required
def podiums2019(current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    cur = conn.cursor()
    cur.execute("SELECT Driver_name,Podiums FROM Drivers2019 ORDER BY Podiums DESC")
    data = cur.fetchall()
    cur.execute("SELECT Team,Podiums FROM Constructors2019 ORDER BY Podiums DESC")
    data1 = cur.fetchall()
    cur.close()
    PodiumsD = []
    PodiumsC = []
    PodiumsD.append({
        data[0][0] : data[0][1],
        data[1][0] : data[1][1],
        data[2][0] : data[2][1],
        data[3][0] : data[3][1],
        data[4][0] : data[4][1],
        data[5][0] : data[5][1],
        data[6][0] : data[6][1],
        data[7][0] : data[7][1],
        data[8][0] : data[8][1],
        data[9][0] : data[9][1],
        data[10][0] : data[10][1],
        data[11][0] : data[11][1],
        data[12][0] : data[12][1],
        data[13][0] : data[13][1],
        data[14][0] : data[14][1],
        data[15][0] : data[15][1],
        data[16][0] : data[16][1],
        data[17][0] : data[17][1],
        data[18][0] : data[18][1],
        data[19][0] : data[19][1]  
           
    })
    PodiumsC.append({
        data1[0][0] : data1[0][1],
        data1[1][0] : data1[1][1],
        data1[2][0] : data1[2][1],
        data1[3][0] : data1[3][1],
        data1[4][0] : data1[4][1],
        data1[5][0] : data1[5][1],
        data1[6][0] : data1[6][1],
        data1[7][0] : data1[7][1],
        data1[8][0] : data1[8][1],
        data1[9][0] : data1[9][1],
        
    })
    return jsonify({'podiums by teams' : PodiumsC},{'podiums by drivers' : PodiumsD})

@app.route('/api/Wins2019')
@token_required
def wins2019(current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    cur = conn.cursor()
    cur.execute("SELECT Driver_name,Wins FROM Drivers2019 ORDER BY Wins DESC")
    data = cur.fetchall()
    cur.execute("SELECT Team,Wins FROM Constructors2019 ORDER BY Wins DESC")
    data1 = cur.fetchall()
    cur.close()
    WinsD = []
    WinsC = []
    WinsD.append({
        data[0][0] : data[0][1],
        data[1][0] : data[1][1],
        data[2][0] : data[2][1],
        data[3][0] : data[3][1],
        data[4][0] : data[4][1],
        data[5][0] : data[5][1],
        data[6][0] : data[6][1],
        data[7][0] : data[7][1],
        data[8][0] : data[8][1],
        data[9][0] : data[9][1],
        data[10][0] : data[10][1],
        data[11][0] : data[11][1],
        data[12][0] : data[12][1],
        data[13][0] : data[13][1],
        data[14][0] : data[14][1],
        data[15][0] : data[15][1],
        data[16][0] : data[16][1],
        data[17][0] : data[17][1],
        data[18][0] : data[18][1],
        data[19][0] : data[19][1],   
           
    })
    WinsC.append({
        data1[0][0] : data1[0][1],
        data1[1][0] : data1[1][1],
        data1[2][0] : data1[2][1],
        data1[3][0] : data1[3][1],
        data1[4][0] : data1[4][1],
        data1[5][0] : data1[5][1],
        data1[6][0] : data1[6][1],
        data1[7][0] : data1[7][1],
        data1[8][0] : data1[8][1],
        data1[9][0] : data1[9][1],
        
    })
    return jsonify({'wins by teams' : WinsC},{'wins by drivers' : WinsD})

@app.route('/api/Points2019')
@token_required
def points2019(current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    cur = conn.cursor()
    cur.execute("SELECT Driver_name,Points FROM Drivers2019 ORDER BY Points DESC")
    data = cur.fetchall()
    cur.execute("SELECT Team,Points FROM Constructors2019 ORDER BY Points DESC")
    data1 = cur.fetchall()
    cur.close()
    PointsD = []
    PointsC = []
    PointsD.append({
        data[0][0] : data[0][1],
        data[1][0] : data[1][1],
        data[2][0] : data[2][1],
        data[3][0] : data[3][1],
        data[4][0] : data[4][1],
        data[5][0] : data[5][1],
        data[6][0] : data[6][1],
        data[7][0] : data[7][1],
        data[8][0] : data[8][1],
        data[9][0] : data[9][1],
        data[10][0] : data[10][1],
        data[11][0] : data[11][1],
        data[12][0] : data[12][1],
        data[13][0] : data[13][1],
        data[14][0] : data[14][1],
        data[15][0] : data[15][1],
        data[16][0] : data[16][1],
        data[17][0] : data[17][1],
        data[18][0] : data[18][1],
        data[19][0] : data[19][1]   
    })
    PointsC.append({
        data1[0][0] : data1[0][1],
        data1[1][0] : data1[1][1],
        data1[2][0] : data1[2][1],
        data1[3][0] : data1[3][1],
        data1[4][0] : data1[4][1],
        data1[5][0] : data1[5][1],
        data1[6][0] : data1[6][1],
        data1[7][0] : data1[7][1],
        data1[8][0] : data1[8][1],
        data1[9][0] : data1[9][1],
        
    })
    return jsonify({'wins by teams' : PointsC},{'wins by drivers' : PointsD})

@app.route('/api/Pole2019')
@token_required
def pole2019(current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    cur = conn.cursor()
    cur.execute("SELECT Driver_name,Pole_Positions FROM Drivers2019 ORDER BY Pole_Positions DESC")
    data = cur.fetchall()
    cur.execute("SELECT Team,Pole_Positions FROM Constructors2019 ORDER BY Pole_Positions DESC")
    data1 = cur.fetchall()
    cur.close()
    PoleD = []
    PoleC = []
    PoleD.append({
        data[0][0] : data[0][1],
        data[1][0] : data[1][1],
        data[2][0] : data[2][1],
        data[3][0] : data[3][1],
        data[4][0] : data[4][1],
        data[5][0] : data[5][1],
        data[6][0] : data[6][1],
        data[7][0] : data[7][1],
        data[8][0] : data[8][1],
        data[9][0] : data[9][1],
        data[10][0] : data[10][1],
        data[11][0] : data[11][1],
        data[12][0] : data[12][1],
        data[13][0] : data[13][1],
        data[14][0] : data[14][1],
        data[15][0] : data[15][1],
        data[16][0] : data[16][1],
        data[17][0] : data[17][1],
        data[18][0] : data[18][1],
        data[19][0] : data[19][1],   

    })
    PoleC.append({
        data1[0][0] : data1[0][1],
        data1[1][0] : data1[1][1],
        data1[2][0] : data1[2][1],
        data1[3][0] : data1[3][1],
        data1[4][0] : data1[4][1],
        data1[5][0] : data1[5][1],
        data1[6][0] : data1[6][1],
        data1[7][0] : data1[7][1],
        data1[8][0] : data1[8][1],
        data1[9][0] : data1[9][1],
        
    })
    return jsonify({'pole_positions by teams' : PoleC},{'pole_positions by drivers' : PoleD})

@app.route('/api/flaps2019')
@token_required
def flaps2019(current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    cur = conn.cursor()
    cur.execute("SELECT Driver_name,Fastest_Laps FROM Drivers2019 ORDER BY Fastest_Laps DESC")
    data = cur.fetchall()
    cur.execute("SELECT Team,Fastest_Laps FROM Constructors2019 ORDER BY Fastest_Laps DESC")
    data1 = cur.fetchall()
    cur.close()
    flapsD = []
    flapsC = []
    flapsD.append({
        data[0][0] : data[0][1],
        data[1][0] : data[1][1],
        data[2][0] : data[2][1],
        data[3][0] : data[3][1],
        data[4][0] : data[4][1],
        data[5][0] : data[5][1],
        data[6][0] : data[6][1],
        data[7][0] : data[7][1],
        data[8][0] : data[8][1],
        data[9][0] : data[9][1],
        data[10][0] : data[10][1],
        data[11][0] : data[11][1],
        data[12][0] : data[12][1],
        data[13][0] : data[13][1],
        data[14][0] : data[14][1],
        data[15][0] : data[15][1],
        data[16][0] : data[16][1],
        data[17][0] : data[17][1],
        data[18][0] : data[18][1],
        data[19][0] : data[19][1],   
       
    })
    flapsC.append({
        data1[0][0] : data1[0][1],
        data1[1][0] : data1[1][1],
        data1[2][0] : data1[2][1],
        data1[3][0] : data1[3][1],
        data1[4][0] : data1[4][1],
        data1[5][0] : data1[5][1],
        data1[6][0] : data1[6][1],
        data1[7][0] : data1[7][1],
        data1[8][0] : data1[8][1],
        data1[9][0] : data1[9][1],
        
    })
    return jsonify({'fastest_laps by teams' : flapsC},{'fastest_laps by drivers' : flapsD})


@app.route('/api/driver-team2019')
@token_required
def info2019(current_user):
    user = current_user['username']
    app.logger.debug("Below url is accessed by %s",user)
    cur = conn.cursor()
    cur.execute("SELECT Driver_name,Team FROM Drivers2019")
    data = cur.fetchall()
    
    cur.close()
    list = []
    
    list.append({
        data[0][0] : data[0][1],
        data[1][0] : data[1][1],
        data[2][0] : data[2][1],
        data[3][0] : data[3][1],
        data[4][0] : data[4][1],
        data[5][0] : data[5][1],
        data[6][0] : data[6][1],
        data[7][0] : data[7][1],
        data[8][0] : data[8][1],
        data[9][0] : data[9][1],
        data[10][0] : data[10][1],
        data[11][0] : data[11][1],
        data[12][0] : data[12][1],
        data[13][0] : data[13][1],
        data[14][0] : data[14][1],
        data[15][0] : data[15][1],
        data[16][0] : data[16][1],
        data[17][0] : data[17][1],
        data[18][0] : data[18][1],
        data[19][0] : data[19][1],  
        
    })

    return jsonify({'drivers - team' : list} )

#