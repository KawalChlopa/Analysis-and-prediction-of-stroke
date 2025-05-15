import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location


def Age(con):
    result = con.execute("""SELECT ac.name as 'Age group', SUM(CASE WHEN i.had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total 
                         FROM Indicators i 
                         INNER JOIN AgeCategory ac 
                         ON i.age_category_id = ac.id  
                         GROUP BY ac.name 
                         ORDER BY ac.name""")
    return result



def Sex(con):
    result = con.execute("""
                         SELECT sex, SUM(CASE WHEN had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as 'total' 
                         FROM Indicators 
                         GROUP BY sex
""")
    return result


def RaceEthnicity(con):
    result = con.execute("""SELECT re.name as 'Race Ethnicty', SUM(CASE WHEN i.had_stroke = TRUE THEN 1 ELSE 0 END) as 'had stroke', COUNT(*) as total 
                         FROM Indicators i 
                         INNER JOIN RaceEthnicityCategory re 
                         ON i.race_ethnicity_category_id = re.id 
                         GROUP BY re.name;
                        """)
    return result


