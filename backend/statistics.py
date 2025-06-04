import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location


special_case = {
    'state_id': 'State',
    'age_category_id': 'AgeCategory',
    'smoker_status_id': 'SmokerStatus',
    'general_health_id': 'GeneralHealth',
    'covid_pos_id': 'CovidPos',
    'ecigarette_usage_id': 'ECigaretteUsage',
    'tetanus_last_10_tdap_id': 'TetanusLast10Tdap',
    'had_diabetes_id': 'HadDiabetes',
    'race_ethnicity_category_id': 'RaceEthnicityCategory',
    'removed_teeth_id': 'RemovedTeeth',
}

def average(con, columns, group=None):
    select_clause = ', '.join([f'ROUND(AVG({col}), 2) as average_{col}' for col in columns])
    query = f"""
    SELECT {select_clause} 
    FROM Indicators 
    WHERE had_heart_attack = 1 
    """
    if group in special_case:
        query = f"""
        SELECT x.name, {select_clause}
        FROM Indicators i
        JOIN {special_case[group]} x ON i.{group} = x.id
        WHERE had_heart_attack = 1
        GROUP BY x.name
        """



    print(f"Executing query: {query}")
    result = con.execute(query)
    return result

def median(con, columns, group=None):
    select_clause = ', '.join([f'ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY {col}), 2) as median_{col}' for col in columns])
    query = f"""
    SELECT {select_clause}
    FROM Indicators
    WHERE had_heart_attack = 1
    """

    if group in special_case:
        query = f"""
        SELECT x.name, {select_clause}
        FROM Indicators i
        JOIN {special_case[group]} x ON i.{group} = x.id
        WHERE had_heart_attack = 1
        GROUP BY x.name
        """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result


def standard_deviation(con, columns, group=None):
    select_clause = ', '.join([f'ROUND(STDDEV({col}), 2) as stddev_{col}' for col in columns])
    query = f"""
    SELECT {select_clause}
    FROM Indicators
    WHERE had_heart_attack = 1
    """
    if group in special_case:
        query = f"""
        SELECT x.name, {select_clause}
        FROM Indicators i
        JOIN {special_case[group]} x ON i.{group} = x.id
        WHERE had_heart_attack = 1
        GROUP BY x.name
        """
    print(f"Executing query: {query}")
    result = con.execute(query)
    return result

def max_value(con, columns, group=None):
    select_clause = ', '.join([f'MAX({col}) as max_{col}' for col in columns])
    query = f"""
    SELECT {select_clause}
    FROM Indicators
    WHERE had_heart_attack = 1
    """
    if group in special_case:
        query = f"""
        SELECT x.name, {select_clause}
        FROM Indicators i
        JOIN {special_case[group]} x ON i.{group} = x.id
        WHERE had_heart_attack = 1
        GROUP BY x.name
        """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result

def min_value(con, columns, group=None):
    select_clause = ', '.join([f'MIN({col}) as min_{col}' for col in columns])
    query = f"""
    SELECT {select_clause}
    FROM Indicators
    WHERE had_heart_attack = 1
    """
    if group in special_case:
        query = f"""
        SELECT x.name, {select_clause}
        FROM Indicators i
        JOIN {special_case[group]} x ON i.{group} = x.id
        WHERE had_heart_attack = 1
        GROUP BY x.name
        """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result

def percentile(con, columns, group=None):
    select_clause = ', '.join([f"ROUND(SUM(CASE WHEN {col} = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as percent_{col}" for col in columns])
    query = f"""
    SELECT {select_clause}
    FROM Indicators
    """
    if group in special_case:
        query = f"""
        SELECT x.name, {select_clause}
        FROM Indicators i
        JOIN {special_case[group]} x ON i.{group} = x.id
        GROUP BY x.name
        """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result
def comorbidity(con, columns, group=None):
    if not columns or len(columns) > 6:
        raise ValueError("You must provide between 1 and 3 columns for comorbidity analysis")

    # Build the condition: all selected indicators must be TRUE
    condition = " AND ".join(f"{col} = TRUE" for col in columns)

    query = f"""
    SELECT 
        had_heart_attack,
        COUNT(*) AS count
    FROM Indicators
    WHERE {condition}
    GROUP BY had_heart_attack
    """

    print(f"Executing query: {query}")
    result = con.execute(query)
    return result



def total(con, columns, group=None):
    result = con.execute("""
                         SELECT 
                             COUNT(*) as 'total'
                         FROM Indicators
                         """)
    
    return result