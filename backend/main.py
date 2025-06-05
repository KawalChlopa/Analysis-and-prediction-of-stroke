import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location
from backend import diseases, statistics, total
from keras.models import load_model
model = load_model("persistence/neural_network_model.keras")
from prediction.predict import predict_heart_attack_neural
from flask import request, jsonify

from flask import render_template

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


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/prediction')
def stroke_prediction():
    return render_template('stroke-prediction.html')

@app.route('/predict-stroke', methods=['POST'])
def predict_stroke():
    try:
        input_data = request.get_json()

        if not input_data:
            return jsonify({'error': 'No input data received'}), 400

        # Convert data types properly
        for key, value in input_data.items():
            if isinstance(value, str):
                if value.lower() == 'true':
                    input_data[key] = True
                elif value.lower() == 'false':
                    input_data[key] = False
                elif value.isdigit():
                    input_data[key] = int(value)
                else:
                    try:
                        input_data[key] = float(value)
                    except ValueError:
                        pass  # Keep as string

        print(f"Sanitized input: {input_data}")

        prediction, probability = predict_heart_attack_neural(input_data)

        # Format final response: "Low 0.06%" or "High 97.32%"
        label = "High" if prediction == 1 else "Low"
        formatted_probability = f"{label} {probability * 100:.2f}%"

        return jsonify({'probability': formatted_probability})

    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({'error': str(e)}), 500


def convert(result):
    columns = [col[0] for col in result.description]
    formatted_data = [dict(zip(columns, row)) for row in result.fetchall()]
    return formatted_data


@app.route('/api/Diseases', methods=['GET'])
def get_diseases_grouped_by():
    #     check params existence
    columns_param = request.args.get('columns')
    group_by_param = request.args.get('group_by')
    print(group_by_param)
    if not columns_param:
        return jsonify({'error': 'Missing required parameter: columns'}), 400

    columns_list = columns_param.split(',')
    group_by_param = request.args.get('group_by')

    con = connection()
    if con is None:
        return jsonify({'error': 'Database connection failed'}), 500
    try:
        data = diseases.diseases(con, columns_list, group_by_param)
        if data is None:
            return jsonify({'error': 'Query returned no results'}), 404

        formatted_data = convert(data)
        return jsonify(formatted_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        con.close()

@app.route('/api/Statistics', methods=['GET'])
def get_statistics():

    statistic = {
        'average': 'average',
        'median': 'median',
        'stddev': 'standard_deviation',
        'max': 'max_value',
        'min': 'min_value',
        'percentile': 'percentile',
        'total': 'total',
        'comorbidity': 'comorbidity'
    }

    columns_param = request.args.get('columns')
    group_by_param = request.args.get('group_by')
    statistic_param = request.args.get('statistic')

    if not columns_param or not statistic_param:
        return jsonify({'error': 'Missing required parameters: columns or statistic'}), 400
    columns_list = columns_param.split(',')

    if statistic_param not in statistic:
        return jsonify({'error': 'Invalid statistic parameter'}), 400
    
    con = connection()
    if con is None:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        
        func_name = statistic.get(statistic_param, None)
        func = getattr(statistics, func_name)
        data = func(con, columns_list, group_by_param)

        if data is None:
            return jsonify({'error': 'Query returned no results'}), 404
        

        formatted_data = convert(data)
        return jsonify(formatted_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        con.close()



if __name__ == '__main__':
    app.run(debug=True)
    con = connection()



