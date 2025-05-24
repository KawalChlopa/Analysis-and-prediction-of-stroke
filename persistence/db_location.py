import os


def get_location():
    cwd = os.getcwd()
    parent_dir = os.path.dirname(cwd)
    db_location = os.path.join(parent_dir,'Analysis-and-prediction-of-stroke', 'persistence', 'stroke-dataset.db')
    return db_location
