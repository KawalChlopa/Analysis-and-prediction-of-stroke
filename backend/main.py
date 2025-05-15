import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location
from . import health_condition
from . import lifestyle
from . import demographic
from . import total


app = Flask(__name__)

def connection():
    path = db_location.get_location()
    print(f"Database path: {path}")
    con = dd.connect(path)
    if con is not None:
        print('Connection successful')
        return con
    else:
        print('Connection failed')
    
def convert(result):
    columns = [col[0] for col in result.description]
    formatted_data = [dict(zip(columns, row)) for row in result.fetchall()]
    print(formatted_data)
    return formatted_data


# Demographic
@app.route('/api/Age', methods=['GET'])
def get_age():
    con = connection()
    
    data = demographic.Age(con)
    formatted_data = convert(data)
    return jsonify(formatted_data)

@app.route('/api/Sex', methods=['GET'])
def Sex():
    con = connection()

    data = demographic.Sex(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/RaceEthnicity', methods=['GET'])
def RaceEthnicity():
    con = connection()

    data = demographic.RaceEthnicity(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

# Lifestyle
@app.route('/api/Smokers', methods=['GET'])
def Smokers():
    con = connection()

    data = lifestyle.Smokers(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/Sleep', methods=['GET'])
def Sleep():
    con = connection()

    data = lifestyle.Sleep(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/BMI', methods=['GET'])
def BMI():
    con = connection()

    data = lifestyle.BMI(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/GeneralHealth', methods=['GET'])
def GeneralHealth():
    con = connection()

    data = lifestyle.GeneralHealth(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)     

# Health Conditions
@app.route('/api/HealthConditions', methods=['GET'])
def HealthConditions():
    con = connection()

    data = health_condition.HealthConditions(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/Asthma', methods=['GET'])
def Asthma():
    con = connection()

    data = health_condition.Asthma(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/KidneyDisease', methods=['GET'])
def KidneyDisease():
    con = connection()

    data = health_condition.KidneyDisease(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/SkinCancer', methods=['GET'])
def SkinCancer():
    con = connection()

    data = health_condition.SkinCancer(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/Angina', methods=['GET'])
def Angina():
    con = connection()

    data = health_condition.Angina(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/Covid_Pos', methods=['GET'])
def Covid_Pos():
    con = connection()

    data = health_condition.Covid_Pos(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)


    return jsonify(formatted_data)

@app.route('/api/HeartDisease', methods=['GET'])
def HeartDisease():
    con = connection()

    data = health_condition.HeartDisease(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

@app.route('/api/Stroke', methods=['GET'])
def Stroke():
    con = connection()

    data = health_condition.Stroke(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

# Total
@app.route('/api/Total', methods=['GET'])
def Total():
    con = connection()

    data = total.Total(con)
    formatted_data = convert(data)

    return jsonify(formatted_data)

if __name__ == '__main__':
    app.run(debug=True)
    con = connection()



