import duckdb as dd
import os
import numpy as np

cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
db_location = os.path.join(parent_dir, 'persistence', 'stroke-dataset.db')
print(db_location)

# Create a persistent DuckDB database
con = dd.connect(db_location)



con.close()
