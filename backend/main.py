import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location
from . import health_condition
from . import lifestyle
from . import demographic
from . import total
from . import diseases
from flask import render_template  # already imported jsonify

endpoint_map = {
    # Demographic
    'Age': demographic.Age,
    'Sex': demographic.Sex,
    'RaceEthnicity': demographic.RaceEthnicity,
    'State': demographic.State,
    # Lifestyle
    'Smokers': lifestyle.Smokers,
    'Sleep': lifestyle.Sleep,
    'BMI': lifestyle.BMI,
    'GeneralHealth': lifestyle.GeneralHealth,
    # Health Conditions
    'Asthma': health_condition.Asthma,
    'KidneyDisease': health_condition.KidneyDisease,
    'SkinCancer': health_condition.SkinCancer,
    'Angina': health_condition.Angina,
    'Covid_Pos': health_condition.Covid_Pos,
    'HeartDisease': health_condition.HeartDiesiese,
    'Stroke': health_condition.Stroke,
    # Total
    'Total': total.Total,
    # Diseases
    'Diseases': diseases.diseases
}


app = Flask(__name__, template_folder='../templates')

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


@app.route('/api/<endpoint>', methods=['GET'])
def api(endpoint):
    con = connection()
    func = endpoint_map.get(endpoint)
    columns_param = request.args.get('columns')

    if func is None:
        return jsonify({'error': 'Endpoint not found'}), 404

    if columns_param is not None:
        columns_params = columns_param.split(',') if columns_param else []
        data = func(con, columns_params)
    else:
        data = func(con)
    
    formatted_data = convert(data)
    return jsonify(formatted_data)

if __name__ == '__main__':
    app.run(debug=True)
    con = connection()



