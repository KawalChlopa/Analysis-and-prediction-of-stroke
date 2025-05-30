import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location

#
def diseases(con, columns, group):
    columns = [
        f"SUM(CASE WHEN {col} = TRUE THEN 1 ELSE 0 END) as {col}"
        for col in columns
    ]
    # Start query differently based on group type
    if group in ['bmi', 'weight_in_kilograms', 'sex']:
        query = f"""
        SELECT Indicators.{group} as name, {", ".join(columns)}
        FROM Indicators
        WHERE had_stroke = 1
        GROUP BY Indicators.{group};
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
            query += "JOIN GeneralHealth x ON Indicators.state_id = x.id"
        elif group == 'race_id':
            query += "JOIN RaceEthnicityCategory x ON Indicators.state_id = x.id"
        elif group == 'ecigarette_usage_id':
            query += "JOIN ECigaretteUsage x ON Indicators.state_id = x.id"
        elif group == 'covid_pos_id':
            query += "JOIN CovidPos x ON Indicators.state_id = x.id"

        query += """
        WHERE had_stroke = 1
        GROUP BY x.name;
        """

    print(f"Executing query: {query}")
    result = con.execute(query)

    return result
# example url:
# http://127.0.0.1:5000/api/Diseases?columns=had_skin_cancer,had_copd,had_depressive_disorder,had_kidney_disease&group_by=state_id