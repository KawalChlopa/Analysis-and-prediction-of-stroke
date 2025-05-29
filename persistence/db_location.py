import os


def get_location():
    current_script_path = os.path.abspath(__file__)

    parent_dir = os.path.dirname(current_script_path)
    root_dir = os.path.dirname(parent_dir)

    db_location = os.path.join(root_dir, 'persistence', 'stroke-dataset.db')
    print(parent_dir)
    print(db_location)
    return db_location
