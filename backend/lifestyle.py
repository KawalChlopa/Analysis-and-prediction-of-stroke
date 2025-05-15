import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location




def Smokers(con):
    result = con.execute("""
                         SELECT 
                         ss.name as 'Smoking Status',
                         SUM(CASE WHEN had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke',
                         COUNT(*) as total
                         FROM Indicators i 
                         INNER JOIN SmokerStatus ss ON i.smoker_status_id = ss.id 
                         GROUP BY smoker_status_id, ss.name
                         """)

    
    return result



def Sleep(con):
    result = con.execute("""SELECT sleep_hours as 'Sleep Hours', SUM(CASE WHEN had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total 
                         FROM Indicators 
                         GROUP BY sleep_hours
                        """)
    return result

def BMI(con):
    result = con.execute("""SELECT bmi as 'BMI', SUM(CASE WHEN had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total 
                         FROM Indicators 
                         GROUP BY bmi
                        """)
    return result

def GeneralHealth(con):
    result = con.execute("""SELECT gh.name, SUM(CASE WHEN i.had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total 
                         FROM Indicators i 
                         INNER JOIN GeneralHealth gh 
                         ON i.general_health_id=gh.id 
                         GROUP BY gh.name
                        """)
    return result
