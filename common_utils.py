from datetime import datetime
import json
import os


def convert_to_timestamp(time_str: str):
    """
    Return a POSIX timestamp 

    Parameters:
    - `time_str` (str): a string representing a datetime following the following formats:
        - "%Y-%m-%dT%H:%M:%S.%fZ"
        - "%Y-%m-%dT%H:%M:%SZ"
        - "%Y:%m:%d %H:%M:%S"
        - "%Y%m%dT%H%M%S.%fZ"
    """
    date_formats = ["%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ",
                    "%Y:%m:%d %H:%M:%S", "%Y%m%dT%H%M%S.%fZ"]
    datetime_obj = None
    for date_format in date_formats:
        try:
            datetime_obj = datetime.strptime(time_str, date_format)
            break
        except ValueError:
            continue
    if datetime is None:
        print("The input Datetime format is not recognized")
    else:
        return datetime_obj.timestamp()


def load_timeline(input_file_path):
    """
    Returns the timeline

    Parameters:
        - `input_file_path` (str): path to the input file

    Returns: a dictionary representing the timeline
    """
    with open(input_file_path, 'r') as json_file:
        try:
            maps_json = json.load(json_file)
        except json.JSONDecodeError:
            print(f"Error parsing JSON in file: {input_file_path}")
    return maps_json


def find_subfolders(input_dir_path):
    """
    Returns a list of all subfolders under the input directory

    Parameters:
        - `input_dir_path` (str): the path to the input directory

    Returns: a list of all subfolders under the input directory
    """
    subfolders = [f for f in os.listdir(
        input_dir_path) if os.path.isdir(os.path.join(input_dir_path, f))]
    return subfolders
