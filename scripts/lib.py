import os
import csv
import json
import requests
import pandas as pd

full_file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(full_file_path)

CONFIG_FILE_PATH = f'{dir_name}/../config.json'
DATA_DICTIONARY_FILE_PATH = f'{dir_name}/../DataDictionary.csv'

def load_config():
    print("Loading Configuration file...")
    with open(CONFIG_FILE_PATH, 'r') as config_file:
        config_text = config_file.read()
    
    config = json.loads(config_text)
    return config


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

def upload_data():
    data = pd.read_csv(DATA_DICTIONARY_FILE_PATH)
    config = load_config()
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
    
def download_data_dictionary(main=False):
    config = load_config()
    redcap_url = 'https://redcap.miami.edu/api/'

    base = config['test_token'] if main is False else config['main_token']
    request_data = {
            'token': base,
            'content': 'metadata',
            'format': 'json',
            'returnFormat': 'json'
            }
    
    print("Downloading dictionary...")
    response = requests.post(redcap_url, request_data)

    json_to_csv(response.text)
    print("Done")


def upload_data_dictionary():
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
    
