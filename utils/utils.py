from datetime import timedelta
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
    
def convert_to_timedelta(time_str):
    """Convert a time string in the format 'HH:MM:SS.ss' to timedelta, ensuring two digits for milliseconds."""
    # Split the time string into hours, minutes, and seconds (including milliseconds)
    
    time_parts = time_str.split(':')
    
    # Check if milliseconds are included in the seconds part
    if '.' in time_parts[2]:
        seconds, milliseconds = time_parts[2].split('.')
        milliseconds = milliseconds.ljust(3, '0')[:3]  # Ensure 3 digits for milliseconds
        time_parts[2] = seconds  # Update seconds part to remove milliseconds

        return timedelta(
            hours=int(time_parts[0]),
            minutes=int(time_parts[1]),
            seconds=int(time_parts[2]),
            milliseconds=int(milliseconds)
        )
    else:
        # If no milliseconds, just return the timedelta with hours, minutes, and seconds
        return timedelta(
            hours=int(time_parts[0]),
            minutes=int(time_parts[1]),
            seconds=int(time_parts[2])
        )

    
