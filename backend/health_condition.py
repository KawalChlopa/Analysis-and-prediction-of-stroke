import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location


def HeartDiesiese(con):
    result = con.execute("""
                        SELECT had_heart_attack as 'Had Heart Attack', SUM(CASE WHEN had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total
                        FROM Indicators
                        GROUP BY had_heart_attack
                        """)
    
    
    return result

def Asthma(con):
    result = con.execute("""SELECT had_asthma as 'Had Asthma', SUM(CASE WHEN had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total 
                         FROM Indicators 
                         GROUP BY had_asthma
                        """)
    
    return result

def KidneyDisease(con):
    result = con.execute("""
                        SELECT had_kidney_disease as 'Had Kidney Disease', SUM(CASE WHEN had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total
                        FROM Indicators
                        GROUP BY had_kidney_disease
                        """)
    
    
    return result

def SkinCancer(con):
    result = con.execute("""SELECT had_skin_cancer as 'skin cancer', SUM(CASE WHEN had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total 
                         FROM Indicators 
                         GROUP BY had_skin_cancer;""")
    
    return result

def Angina(con):
    result = con.execute("""
                        SELECT had_angina as 'Had Angina', SUM(CASE WHEN had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total
                        FROM Indicators
                        GROUP BY had_angina
                        """)
    
    
    return result

def Covid_Pos(con):
    result = con.execute("""
                        SELECT cp.name as 'Had Covid', SUM(CASE WHEN i.had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total 
                         FROM Indicators i 
                         INNER JOIN CovidPos cp 
                         ON cp.id = i.covid_pos_id 
                         GROUP BY cp.name
                        """)
    
    
    return result

def Stroke(con):
    result = con.execute("""
                        SELECT had_stroke as 'Had Stroke', COUNT(*) as total
                        FROM Indicators
                        GROUP BY had_stroke
                        """)
    
    
    return result



    




