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
    
    else:
        print('Connection failed')
    
@app.route('/all_data', methods=['GET'])
def all_data():
    con = connection()
    data = con.execute('SELECT * FROM countries').fetchall()
    return jsonify(data)

@app.route('/age', methods=['GET'])
def age():
    con = connection()

    age = request.args.get('age')
    country = request.args.get('country')
    
    query = "SELECT * FROM AgeCategory"
    params = []

    if age and country:
        query += " WHERE age = ? AND country = ?"
        params.extend([age, country])
        data = con.execute(query, params).fetchall()
    elif age:
        query += " WHERE age = ?"
        params.append(age)
        data = con.execute(query, params).fetchall()
    elif country:
        query += " WHERE country = ?"
        params.append(country)
        data = con.execute(query, params).fetchall()
    else:
        data = con.execute(query).fetchall()
    return jsonify(data)

@app.route('/general_health', methods=['GET'])
def general_health():
    con = connection()

    health = request.args.get('health')
    params = []
    query = "SELECT * FROM GeneralHealth"
    if health:
        query += " WHERE health = ?"
        params.append(health)
        data = con.execute(query, params).fetchall()
    else:
        data = con.execute(query)
    return jsonify(data)

@app.route('/EcigaretteUsage', methods=['GET'])
def ecigarette_usage():
    con = connection()

    
    query = "SELECT * FROM EcigaretteUsage"
    params = []

@app.route('/CovidPos', methods=['GET'])
def covid_pos():
    con = connection()

    query = "SELECT * FROM CovidPos"
    params = []

@app.route('/HadDiabetes', methods=['GET'])
def had_diabetes():
    con = connection()

    query = "SELECT * FROM HadDiabetes"
    params = []

@app.route('/Indicators', methods=['GET'])
def indicators():
    con = connection()

    query = "SELECT * FROM Indicators"
    params = []

@app.route('/RaceEthnicityCategory', methods=['GET'])
def race_ethnicity_category():
    con = connection()

    query = "SELECT * FROM RaceEthnicityCategory"
    params = []

@app.route('/RemovedTeeth', methods=['GET'])
def removed_teeth():
    con = connection()

    query = "SELECT * FROM RemovedTeeth"
    params = []

@app.route('/SmokerStatus', methods=['GET'])
def smoker_status():
    con = connection()

    query = "SELECT * FROM SmokerStatus"
    params = []

@app.route('/States', methods=['GET'])
def states():
    con = connection()

    query = "SELECT * FROM States"
    params = []

@app.route('/TetanusLast10Tdap', methods=['GET'])
def tetanus_last_10_tdap():
    con = connection()

    query = "SELECT * FROM TetanusLast10Tdap"
    params = []





# app.run(debug=True) 

connection()
