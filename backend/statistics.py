import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location

def connection():
    path = db_location.get_location()
    print(f"Database path: {path}")
    con = dd.connect(path)
    if con is not None:
        print('Connection successful')
        return con
    else:
        print('Connection failed')


def average(con, columns, group):
    select_clause = ', '.join([f'ROUND(AVG({col}), 2) as average_{col}' for col in columns])
    query = f"""
    SELECT {group}, {select_clause} 
    FROM Indicators 
    WHERE had_heart_attack = 1 
    GROUP BY {group}
    """
    if group == 'state_id':
        query = f"""
        SELECT s.name as State, {select_clause}
        FROM Indicators i
        JOIN State s ON i.state_id = s.id
        WHERE had_heart_attack = 1
        GROUP BY s.name
        """
    elif group == 'age_category_id':
        query = f"""
        SELECT ac.name as AgeCategory, {select_clause}
        FROM Indicators i
        JOIN AgeCategory ac ON i.age_category_id = ac.id
        WHERE had_heart_attack = 1
        GROUP BY ac.name
        """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result

def median(con, columns, group):
    select_clause = ', '.join([f'ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY {col}), 2) as median_{col}' for col in columns])
    query = f"""
    SELECT {group}, {select_clause}
    FROM Indicators
    WHERE had_heart_attack = 1
    GROUP BY {group}
    """

    if group == 'state_id':
        query = f"""
        SELECT s.name as State, {select_clause}
        FROM Indicators i
        JOIN State s ON i.state_id = s.id
        WHERE had_heart_attack = 1
        GROUP BY s.name
        """
    elif group == 'age_category_id':
        query = f"""
        SELECT ac.name as AgeCategory, {select_clause}
        FROM Indicators i
        JOIN AgeCategory ac ON i.age_category_id = ac.id
        WHERE had_heart_attack = 1
        GROUP BY ac.name
        """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result


def standard_deviation(con, columns, group):
    select_clause = ', '.join([f'ROUND(STDDEV({col}), 2) as stddev_{col}' for col in columns])
    query = f"""
    SELECT {group}, {select_clause}
    FROM Indicators
    WHERE had_heart_attack = 1
    GROUP BY {group}
    """
    if group == 'state_id':
        query = f"""
        SELECT s.name as State, {select_clause}
        FROM Indicators i
        JOIN State s ON i.state_id = s.id
        WHERE had_heart_attack = 1
        GROUP BY s.name
        """
    elif group == 'age_category_id':
        query = f"""
        SELECT ac.name as AgeCategory, {select_clause}
        FROM Indicators i
        JOIN AgeCategory ac ON i.age_category_id = ac.id
        WHERE had_heart_attack = 1
        GROUP BY ac.name
        """
    print(f"Executing query: {query}")
    result = con.execute(query)
    return result

def max_value(con, columns, group):
    select_clause = ', '.join([f'MAX({col}) as max_{col}' for col in columns])
    query = f"""
    SELECT {group}, {select_clause}
    FROM Indicators
    WHERE had_heart_attack = 1
    GROUP BY {group}
    """
    if group == 'state_id':
        query = f"""
        SELECT s.name as State, {select_clause}
        FROM Indicators i
        JOIN State s ON i.state_id = s.id
        WHERE had_heart_attack = 1
        GROUP BY s.name
        """
    elif group == 'age_category_id':
        query = f"""
        SELECT ac.name as AgeCategory, {select_clause}
        FROM Indicators i
        JOIN AgeCategory ac ON i.age_category_id = ac.id
        WHERE had_heart_attack = 1
        GROUP BY ac.name
        """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result

def min_value(con, columns, group):
    select_clause = ', '.join([f'MIN({col}) as min_{col}' for col in columns])
    query = f"""
    SELECT {group}, {select_clause}
    FROM Indicators
    WHERE had_heart_attack = 1
    GROUP BY {group}
    """
    if group == 'state_id':
        query = f"""
        SELECT s.name as State, {select_clause}
        FROM Indicators i
        JOIN State s ON i.state_id = s.id
        WHERE had_heart_attack = 1
        GROUP BY s.name
        """
    elif group == 'age_category_id':
        query = f"""
        SELECT ac.name as AgeCategory, {select_clause}
        FROM Indicators i
        JOIN AgeCategory ac ON i.age_category_id = ac.id
        WHERE had_heart_attack = 1
        GROUP BY ac.name
        """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result

def percentile(con, columns, group):
    select_clause = ', '.join([f"CAST(ROUND(SUM(CASE WHEN {col} = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS VARCHAR) || '%' as percent_{col}" for col in columns])
    query = f"""
    SELECT {group}, {select_clause}
    FROM Indicators
    GROUP BY {group}
    """
    if group == 'state_id':
        query = f"""
        SELECT s.name as State, {select_clause}
        FROM Indicators i
        JOIN State s ON i.state_id = s.id
        GROUP BY s.name
        """
    elif group == 'age_category_id':
        query = f"""
        SELECT ac.name as AgeCategory, {select_clause}
        FROM Indicators i
        JOIN AgeCategory ac ON i.age_category_id = ac.id
        GROUP BY ac.name
        """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result