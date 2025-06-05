import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location

def diseases(con, columns, group):
    columns = [
        f"SUM(CASE WHEN {col} = TRUE THEN 1 ELSE 0 END) as {col}"
        for col in columns
    ]
    # Start query differently based on group type
    if group == 'weight_in_kilograms':
        query = f"""
        SELECT FLOOR(Indicators.weight_in_kilograms / 5) * 5 AS name, {", ".join(columns)}
        FROM Indicators
        WHERE had_heart_attack = 1
        GROUP BY FLOOR(Indicators.weight_in_kilograms / 5) * 5
        ORDER BY name;
        """
    elif group == 'bmi':
        query = f"""
        SELECT FLOOR(Indicators.bmi / 5) * 5 AS name, {", ".join(columns)}
        FROM Indicators
        WHERE had_heart_attack = 1
        GROUP BY FLOOR(Indicators.bmi / 5) * 5
        ORDER BY name;
        """
    elif group == 'sex':
        query = f"""
        SELECT Indicators.sex as name, {", ".join(columns)}
        FROM Indicators
        WHERE had_heart_attack = 1
        GROUP BY Indicators.sex
        ORDER BY Indicators.sex;
        """
    else:
        query = f"""
        SELECT x.name, {", ".join(columns)}
        FROM Indicators
        """

        if group == 'age_category_id':
            query += "JOIN AgeCategory x ON Indicators.age_category_id = x.id"
        elif group == 'state_id':
            query += "JOIN State x ON Indicators.state_id = x.id"
        elif group == 'general_health_id':
            query += "JOIN GeneralHealth x ON Indicators.general_health_id = x.id"
        elif group == 'race_id':
            query += "JOIN RaceEthnicityCategory x ON Indicators.race_ethnicity_category_id = x.id"
        elif group == 'ecigarette_usage_id':
            query += "JOIN ECigaretteUsage x ON Indicators.ecigarette_usage_id = x.id"
        elif group == 'covid_pos_id':
            query += "JOIN CovidPos x ON Indicators.covid_pos_id = x.id"

        query += """
        WHERE had_heart_attack = 1
        GROUP BY x.name
        ORDER BY x.name;
        """

    print(f"Executing query: {query}")
    result = con.execute(query)

    return result
# example url:
# http://127.0.0.1:5000/api/Diseases?columns=had_skin_cancer,had_copd,had_depressive_disorder,had_kidney_disease&group_by=state_id