#!/usr/bin/env python3


import csv
import json

def convert_csv_to_json(csv_filename):
    try:
         
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        # Return False if file not found
        return False
    
    except Exception:
        # Return False for any other errors
        return False
