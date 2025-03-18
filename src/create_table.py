import duckdb as dd
import os
import numpy as np

cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
db_location = os.path.join(parent_dir, 'persistence', 'stroke-dataset.db')
print(db_location)

# Create a persistent DuckDB database
con = dd.connect(db_location)



# Create a table
con.execute('''
CREATE OR REPLACE TABLE countries (
    state VARCHAR,
    sex BOOLEAN,
    general_health VARCHAR,
    physical_health_days INT,
    mental_health_days INT,
    physical_activities BOOLEAN,
    sleep_hours INT,
    removed_teeth VARCHAR,
    had_heart_attack BOOLEAN,
    had_angina BOOLEAN,
    had_stroke BOOLEAN,
    had_asthma BOOLEAN,
    had_skin_cancer BOOLEAN,
    had_copd BOOLEAN,
    had_depressive_disorder BOOLEAN,
    had_kidney_disease BOOLEAN,
    had_arthritis BOOLEAN,
    had_diabetes VARCHAR,
    deaf_or_hard_of_hearing BOOLEAN,
    blind_or_vision_difficulty BOOLEAN,
    difficulty_concentrating BOOLEAN,
    difficulty_walking BOOLEAN,
    difficulty_dressing_bathing BOOLEAN,
    difficulty_errands BOOLEAN,
    smoker_status VARCHAR,
    ecigarette_usage VARCHAR,
    chest_scan BOOLEAN,
    race_ethnicity_category VARCHAR,
    age_category VARCHAR,
    height_in_cm INT,
    weight_in_kilograms DOUBLE,
    bmi DOUBLE,
    alcohol_drinkers BOOLEAN,
    hiv_testing BOOLEAN,
    flu_vax_last_12 BOOLEAN,
    pneumo_vax_ever BOOLEAN,
    tetanus_last_10_tdap VARCHAR,
    high_risk_last_year BOOLEAN,
    covid_pos VARCHAR
);
''')

con.close()
