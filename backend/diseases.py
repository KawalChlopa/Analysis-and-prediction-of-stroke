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
