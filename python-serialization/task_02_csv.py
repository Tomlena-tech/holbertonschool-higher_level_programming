#!/usr/bin/env python3
"""Module for converting CSV data to JSON format"""


import csv
import json

def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and save to data.json"""
    try:
         
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    
    except FileNotFoundError:
        
        return False
    
    except Exception:
        
        return False
