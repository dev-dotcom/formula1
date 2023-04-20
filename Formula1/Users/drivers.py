from Formula1 import app
from flask import render_template

@app.route('/pages/LewisHamilton')
def one():
    return render_template('/pages/LewisHamilton.html')

@app.route('/pages/SebastianVettel')
def two():
    return render_template('/pages/SebastianVettel.html')

@app.route('/pages/KimiRäikkönen')
def three():
    return render_template('/pages/KimiRäikkönen.html')

@app.route('/pages/MaxVerstappen')
def four():
    return render_template('/pages/MaxVerstappen.html')

@app.route('/pages/ValtteriBottas')
def five():
    return render_template('/pages/ValtteriBottas.html')

@app.route('/pages/DanielRicciardo')
def six():
    return render_template('/pages/DanielRicciardo.html')

@app.route('/pages/NicoHulkenberg')
def seven():
    return render_template('/pages/NicoHulkenberg.html')

@app.route('/pages/SergioPerez')
def eight():
    return render_template('/pages/SergioPerez.html')

@app.route('/pages/KevinMagnussen')
def nine():
    return render_template('/pages/KevinMagnussen.html')

@app.route('/pages/CarlosSainz')
def ten():
    return render_template('/pages/CarlosSainz.html')

@app.route('/pages/FernandoAlonso')
def eleven():
    return render_template('/pages/FernandoAlonso.html')

@app.route('/pages/EstebanOcon')
def thirteen():
    return render_template('/pages/EstebanOcon.html')

@app.route('/pages/CharlesLeclerc')
def fourteen():
    return render_template('/pages/CharlesLeclerc.html')

@app.route('/pages/RomainGrosjean')
def fifteen():
    return render_template('/pages/RomainGrosjean.html')

@app.route('/pages/PierreGasly')
def sixteen():
    return render_template('/pages/PierreGasly.html')

@app.route('/pages/LanceStroll')
def seventeen():
    return render_template('/pages/LanceStroll.html')

