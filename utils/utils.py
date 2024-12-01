import importlib
import os
from random import randint

def import_levels(folder_name):
    # Dynamically import all modules in the specified folder
    levels_path = os.path.join(os.path.dirname(__file__), '..', 'src', folder_name)
    excluded_files = {"__init__.py"}

    if not os.path.exists(levels_path):
        raise FileNotFoundError(f"{folder_name} directory not found: {levels_path}")

    modules = {
        f.split(".")[0]: importlib.import_module(f"src.{folder_name}.{f[:-3]}")
        for f in os.listdir(levels_path)
        if f.endswith(".py") and f not in excluded_files
    }
    
    return modules

def set_spawn_rate(from_, to_):
    return randint(from_, to_)

def name_input_validate(name):
        if not name or len(name) > 10:
            return False
        return all(char.isalpha() or char.isdigit() for char in name)