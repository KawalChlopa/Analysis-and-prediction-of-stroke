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