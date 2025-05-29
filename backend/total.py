import duckdb as dd
from flask import Flask, jsonify, request
from persistence import db_location


def Total(con):
    result = con.execute("""
                         SELECT 
                             COUNT(*) as 'total'
                         FROM Indicators
                         """)
    
    return result

