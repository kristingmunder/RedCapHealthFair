import os
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

print("Loading data dictionary...")
data = pd.read_csv(DATA_DICTIONARY_FILE_PATH)

redcap_url = 'https://redcap.miami.edu/api/'

request_data = {
        'token': config['test_token'],
        'content': 'metadata',
        'format': 'json',
        'data': data.to_json(orient='records'),
        'returnFormat': 'json'
        }

print("Attempting to upload the data dictionary...")
response = requests.post(redcap_url, request_data)
print(response.text)
