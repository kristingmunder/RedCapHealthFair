import os
import csv
import json
import requests
import pandas as pd

full_file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(full_file_path)

CONFIG_FILE_PATH = f'{dir_name}/../config.json'
DATA_DICTIONARY_FILE_PATH = f'{dir_name}/../DataDictionary.csv'

print("Loading Configuration file...")
with open(CONFIG_FILE_PATH, 'r') as config_file:
    config_text = config_file.read()

config = json.loads(config_text)

redcap_url = 'https://redcap.miami.edu/api/'

request_data = {
        'token': config['test_token'],
        'content': 'metadata',
        'format': 'json',
        'returnFormat': 'json'
        }

print("Downloading dictionary...")
response = requests.post(redcap_url, request_data)

def json_to_csv(json_text):
    json_data = json.loads(json_text)
    csv_name = DATA_DICTIONARY_FILE_PATH
    with open(csv_name, 'w') as f:
        writer = csv.writer(f)
        keys = []
        for key in json_data[0]:
            keys.append(key)
        writer.writerow(keys)
        for j in json_data:
            values = []
            for key in j:
                values.append(j[key])
            writer.writerow(values)
        return pd.read_csv(csv_name)

json_to_csv(response.text)
print("Done")
