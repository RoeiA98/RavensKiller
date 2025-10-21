from datetime import timedelta
import importlib
import os
from random import randint


def import_levels(folder_name):
    # Dynamically import all modules in the specified folder
    levels_path = os.path.join(os.path.dirname(__file__), "..", "src", folder_name)
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


def time_to_centiseconds(time_str):
    hours, minutes, seconds = time_str.split(":")
    sec, centisec = map(int, seconds.split("."))
    total_centiseconds = (int(hours) * 3600 + int(minutes) * 60 + sec) * 100 + centisec
    return total_centiseconds


def centiseconds_to_time(cs):
    hours = cs // 360000
    cs %= 360000
    minutes = cs // 6000
    cs %= 6000
    seconds = cs // 100
    centisec = cs % 100
    return f"{hours:02}:{minutes:02}:{seconds:02}.{centisec:02}"


def name_input_validate(name):
    if not name or len(name) > 10:
        return False
    return all(char.isalpha() or char.isdigit() for char in name)


def convert_to_timedelta(time_str):
    """Convert a time string in the format 'HH:MM:SS.ss' to timedelta, ensuring two digits for milliseconds."""
    # Split the time string into hours, minutes, and seconds (including milliseconds)

    time_parts = time_str.split(":")

    # Check if milliseconds are included in the seconds part
    if "." in time_parts[2]:
        seconds, milliseconds = time_parts[2].split(".")
        milliseconds = milliseconds.ljust(3, "0")[
            :3
        ]  # Ensure 3 digits for milliseconds
        time_parts[2] = seconds  # Update seconds part to remove milliseconds

        return timedelta(
            hours=int(time_parts[0]),
            minutes=int(time_parts[1]),
            seconds=int(time_parts[2]),
            milliseconds=int(milliseconds),
        )
    else:
        # If no milliseconds, just return the timedelta with hours, minutes, and seconds
        return timedelta(
            hours=int(time_parts[0]),
            minutes=int(time_parts[1]),
            seconds=int(time_parts[2]),
        )


def format_timedelta(td: timedelta) -> str:
    total_seconds = td.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:05.2f}"


def time_str_to_seconds(time_str: str) -> float:
    """Convert a time string in the HH:MM:SS.ss format to total seconds."""
    try:
        hours, minutes, seconds = time_str.split(":")
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    except Exception:
        return float("inf")


def load_env_file(env_path):
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value