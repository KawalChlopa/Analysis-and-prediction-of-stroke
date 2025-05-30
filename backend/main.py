import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location
from backend import diseases, total
from flask import render_template  # already imported jsonify

endpoint_map = {
     # Total
    'Total': total.Total,
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


@app.route('/api/<endpoint>', methods=['GET'])
def api(endpoint):
    con = connection()
    func = endpoint_map.get(endpoint)
    columns_param = request.args.get('columns')

    if func is None:
        return jsonify({'error': 'Endpoint not found'}), 404

    try:
        if columns_param is not None:
            columns_params = columns_param.split(',') if columns_param else []
            data = func(con, columns_params)
        else:
            data = func(con)
    except Exception as ex:
        con.close()

    con.close()
    formatted_data = convert(data)
    return jsonify(formatted_data)


if __name__ == '__main__':
    app.run(debug=True)
    con = connection()



