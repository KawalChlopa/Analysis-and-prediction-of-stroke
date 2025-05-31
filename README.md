# Analysis and prediction of stroke
Academy project

## Overview
The project involves the collection and analysis of medical data from Kaggle – Personal Key Indicators of Heart Disease. Various risk factors for heart attacks, such as cholesterol levels, blood pressure, lifestyle habits, and comorbidities, are examined.

Following data collection, a data cleaning process is conducted, followed by detailed statistical analysis to identify key patterns. Based on the findings, a predictive model is developed to assess the probability of cardiovascular diseases.

## Database access
1. Download a database file from the link: [stroke-dataset.db](https://drive.google.com/drive/folders/1usHHC51Z2WUu4vuUFLm7Dwyt932iyqYv)
2. Place the file in the ./persistence directory

## Run flask
`python -m backend.main`

## Example endpoints:
1. `http://127.0.0.1:5000/api/Diseases?columns=had_skin_cancer,had_copd,had_depressive_disorder,had_kidney_disease&group_by=age_category_id` pull specific count of diseases grouped by specific multivalue column - source ***diseases.py***
2. `http://<average>` pull averages of specified columns
3. `http://127.0.0.1:5000/api/Statistics?columns=bmi&group_by=had_heart_attack&statistic=average` pull average BMI grouped by heart attack status - source ***statistics.py***
4. `http://127.0.0.1:5000/api/Statistics?columns=bmi&group_by=state_id&statistic=average` pull average BMI by state for people with heart attacks - source ***statistics.py***
5. `http://127.0.0.1:5000/api/Statistics?columns=bmi&group_by=had_heart_attack&statistic=max` pull maximum BMI grouped by heart attack status - source ***statistics.py***
6. `http://127.0.0.1:5000/api/Statistics?columns=sleep_hours&group_by=had_heart_attack&statistic=average` pull average sleep hours grouped by heart attack status - source ***statistics.py***
7. `http://127.0.0.1:5000/api/Statistics?columns=height_in_cm&group_by=had_heart_attack&statistic=average` pull average height grouped by heart attack status - source ***statistics.py***
8. `http://127.0.0.1:5000/api/Statistics?columns=height_in_cm&group_by=had_heart_attack&statistic=median` pull median height grouped by heart attack status - source ***statistics.py***
9. `http://127.0.0.1:5000/api/Statistics?columns=height_in_cm&group_by=had_heart_attack&statistic=stddev` pull standard deviation of height grouped by heart attack status - source ***statistics.py***
10. `http://127.0.0.1:5000/api/Statistics?columns=had_heart_attack&group_by=blind_or_vision_difficulty&statistic=percentile` pull percentage of visually impaired people who had heart attacks - source ***statistics.py***
11. `http://127.0.0.1:5000/api/Statistics?columns=had_heart_attack&group_by=age_category_id&statistic=percentile` pull heart attack percentage by age group - source ***statistics.py***
12. `http://127.0.0.1:5000/api/Statistics?columns=had_heart_attack&group_by=had_depressive_disorder&statistic=percentile` pull percentage of people with both heart attacks and depression - source ***statistics.py***


