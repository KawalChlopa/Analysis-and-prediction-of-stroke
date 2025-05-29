import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location


def diseases(con, params):
    columns = [
        f"SUM(CASE WHEN {col} = TRUE THEN 1 ELSE 0 END) as {col.replace('had_', '')}"         
        for col in params     
    ]          
    
    select = ', '.join(columns)
    
    conditions = [f"{col} = TRUE" for col in params if col != 'had_stroke']
    where = ' AND '.join(conditions)
    
    query = f"""         
        SELECT sex, {select}, COUNT(*) as total         
        FROM Indicators 
        WHERE ({where})
        GROUP BY sex     
    """
    
    print(f"Executing query: {query}")
    result = con.execute(query)          
    
    return result
# in above case the where is useles


def chosen_diseases(con, columns, group='sex'):
    columns = [
        f"SUM(CASE WHEN {col} = TRUE THEN 1 ELSE 0 END) as {col}"
        for col in columns
    ]

    query = f"""
      SELECT {group}, {", ".join(columns)}
      FROM Indicators
      WHERE had_stroke = 1
      GROUP BY {group};
    """

    print(f"Executing query: {query}")
    result = con.execute(query)

    return result
# example url:
# http://127.0.0.1:5000/api/Diseases?columns=had_skin_cancer,had_copd,had_depressive_disorder,had_kidney_disease&group_by=state_id