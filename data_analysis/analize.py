import os
import duckdb as dd
import json
from flask import Flask, jsonify, request
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "persistence"))

import fill_db


app = Flask(__name__)

def connection():
    path = fill_db.db_location
    con = dd.connect(path)
    tables = con.execute("SHOW TABLES").fetchall()
    print(tables)
    if con is not None:
        print('Connection successful')
        return con
    else:
        print('Connection failed')
    
@app.route('/all_data', methods=['GET'])
def all_data():
    con = connection()
    data = con.execute('SELECT * FROM countries').fetchall()
    return jsonify(data)

@app.route('/AgeCategory', methods=['GET'])
def AgeCategory():
    
    con = connection()
    
    age_ids = request.args.get('age_ids')    
    print(age_ids)
    
    query = "SELECT * FROM Indicators INNER JOIN AgeCategory ON Indicators.age_category_id = AgeCategory.Id"
    
    if age_ids:
         
        query += (f" WHERE ageCategory.Id IN ({age_ids}) LIMIT 10")
        
        print(query)
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
        
    else:
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)    


    
@app.route('/CovidPos', methods=['GET'])
def CovidPos():
    
    con = connection()
    
    CovidPos_ids = str(request.args.get('CovidPos_ids'))
    print(CovidPos_ids)
    
    query = "SELECT * FROM Indicators INNER JOIN CovidPos ON Indicators.covid_pos_id = CovidPos.Id"
    
    if CovidPos_ids:
        
        query += (f" WHERE CovidPos.Id IN ({CovidPos_ids}) LIMIT 10")
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
    else:
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
        


@app.route('/ECigaretteUsage', methods=['GET'])
def ECigaretteUsage():
    
    con = connection()
    
    ECigaretteUsage_ids = str(request.args.get('ECIgaretteUsage_ids'))
    
    query = "SELECT * FROM Indicators INNER JOIN ECigaretteUsage ON ECigaretteUsage.Id = Indicators.ecigarette_usage_id"

    if ECigaretteUsage:
        
        query += (f" WHERE ECigaretteUsage.Id IN ({ECigaretteUsage_ids}) LIMIT 10")
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
    else:
        
        data = con.execute(quety).fetchall()
        print(data)
        return jsonify(data)
    
@app.route('/GeneralHralth', methods=['GET'])
def GeneralHralth():
    
    con = connection()
    
    GeneralHralth_ids = str(request.args.get('GeneralHralth_ids'))
    
    query = "SELECT * FROM Indicators INNER JOIN GeneralHralth ON GeneralHralth.Id = Indicators.general_health_id"

    if GeneralHralth_ids:
        
        query += (f" WHERE GeneralHralth.Id IN ({GeneralHralth_ids}) LIMIT 10")
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
    else:
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
@app.route('/HadDiabetes', methods=['GET'])
def HadDiabetes():
    
    con = connection()
    
    HadDiabetes_ids = str(request.args.get('HadDiabetes_ids'))
    
    query = "SELECT * FROM Indicators INNER JOIN HadDiabetes ON HadDiabetes.Id = Indicators.had_diabetes_id"

    if HadDiabetes_ids:
        
        query += (f" WHERE HadDiabetes.Id IN ({HadDiabetes_ids}) LIMIT 10")
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
    else:
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
@app.route('/RaceEthnicityCategory', methods=['GET'])
def RaceEthnicityCategory():
    
    con = connection()
    
    RaceEthnicityCategory_ids = str(request.args.get('RaceEthnicityCategory_ids'))
    
    query = "SELECT * FROM Indicators INNER JOIN RaceEthnicityCategory_ids ON RaceEthnicityCategory.Id = Indicators.race_ethnicity_category_id"
    
    if RaceEthnicityCategory:
        
        query += (f" WHERE RaceEthnicityCategory.Id IN ({RaceEthnicityCategory_ids}) LIMIT 10")
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
@app.route('/RemovedTeeth', methods=['GET'])
def RemovedTeeth():
    
    con = connection()
    
    RemovedTeeth_ids = str(request.args.get('RemovedTeeth_ids'))
    
    query = "SELECT * FROM Indicators INNER JOIN RemovedTeeth ON RemovedTeeth.Id = Indicators.removed_teeth_id"

    if RemovedTeeth_ids:
        
        query += (f" WHERE RemovedTeeth.Id IN ({RemovedTeeth_ids}) LIMIT 10")
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
    else:
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    

@app.route('/SmokerStatus', methods=['GET'])
def SmokerStatus():
    
    con = connection()
    
    SmokerStatus_ids = str(request.args.get('SmokerStatus_ids'))
    
    query = "SELECT * FROM Indicators INNER JOIN SmokerStatus ON SmokerStatus.Id = Indicators.smoker_status_id"

    if SmokerStatus_ids:
        
        query += (f" WHERE SmokerStatus.Id IN ({SmokerStatus_ids}) LIMIT 10")
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
    else:
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
@app.route('/State' , methods=['GET'])
def State():
    
    con = connection()
    
    State_ids = str(request.args.get('State_ids'))
    
    query = "SELECT * FROM Indicators INNER JOIN State ON State.Id = Indicators.state_id"

    if State_ids:
        
        query += (f" WHERE State.Id IN ({State_ids}) LIMIT 10")
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
    else:
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
@app.route('/TetanusLast10Tdap', methods=['GET'])
def TetanusLast10Tdap():
    
    con = connection()
    
    TetanusLast10Tdap_ids = str(request.args.get('TetanusLast10Tdap_ids'))
    
    query = "SELECT * FROM Indicators INNER JOIN TetanusLast10Tdap ON TetanusLast10Tdap.Id = Indicators.tetanus_last_10_tdap_id"

    if TetanusLast10Tdap_ids:
        
        query += (f" WHERE TetanusLast10Tdap.Id IN ({TetanusLast10Tdap_ids}) LIMIT 10")
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
    else:
        
        data = con.execute(query).fetchall()
        print(data)
        return jsonify(data)
    
        
app.run(debug=True) 


