import os
import csv
import json
import requests
import pandas as pd

from typing import List

full_file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(full_file_path)

CONFIG_FILE_PATH = f'{dir_name}/../config.json'
DATA_DICTIONARY_DIR = f'{dir_name}/../data'
DATA_DICTIONARY_FILE_PATH = f'{DATA_DICTIONARY_DIR}/DataDictionary.csv'


def load_config() -> dict:
    print("Loading Configuration file...")
    with open(CONFIG_FILE_PATH, 'r') as config_file:
        config_text: str = config_file.read()

    config: dict = json.loads(config_text)
    return config


def check_data_dir():
    if os.path.exists(DATA_DICTIONARY_DIR):
        return

    os.makedirs(DATA_DICTIONARY_DIR)


def json_to_csv(
        json_text,
        file_name=DATA_DICTIONARY_FILE_PATH
        ) -> pd.DataFrame:
    """The reason we have this function is so that we can preserve the order of
    names within the json data. The pandas.to_cvs doesn't allow users to
    disable sorting"""

    json_data: dict = json.loads(json_text)
    csv_name: str = file_name
    with open(csv_name, 'w') as f:
        writer = csv.writer(f)
        keys: list = []
        for key in json_data[0]:
            keys.append(key)
        writer.writerow(keys)
        for j in json_data:
            values: list = []
            for key in j:
                values.append(j[key])
            writer.writerow(values)

    pd_data = pd.read_csv(csv_name)
    os.remove(file_name)

    return pd_data


def upload_to_test_project():
    data = pd.read_csv(DATA_DICTIONARY_FILE_PATH)
    config = load_config()
    redcap_url = 'https://redcap.miami.edu/api/'

    project_name = "Med IT Test Project"
    request_data = {
            'token': config['test_token'],
            'content': 'metadata',
            'format': 'json',
            'data': data.to_json(orient='records'),
            'returnFormat': 'json'
            }

    print(f"Attempting to upload the data dictionary to the {project_name}...")
    response = requests.post(redcap_url, request_data)
    print(response.text)


def download_data_df(main=False) -> pd.DataFrame:
    """This downloads the data dictionary to a dataframe"""
    config = load_config()
    redcap_url = 'https://redcap.miami.edu/api/'

    project_name = "New REDCap" if main is True else "MedIT Test project"
    base = config['test_token'] if main is False else config['main_token']
    request_data = {
            'token': base,
            'content': 'metadata',
            'format': 'json',
            'returnFormat': 'json'
            }

    print(f"Downloading dictionary from {project_name}...")
    response = requests.post(redcap_url, request_data)

    return pd.read_json(response.text)


def split_instrument_dataframe(df: pd.DataFrame) -> list:
    instrument_list: list = list(set(df['form_name']))
    return [df[df['form_name'] == x] for x in instrument_list]


def save_instrument_lists(
        instruments: List[pd.DataFrame],
        directory: str = DATA_DICTIONARY_DIR):
    """Take our instruments and save them as csv"""
    check_data_dir()
    for instrument_df in instruments:
        instrument_name: str = list(set(instrument_df['form_name']))[0]
        instrument_csv_file: str = f'{directory}/{instrument_name}.csv'
        instrument_df.to_csv(instrument_csv_file, index=False)


def read_csv_instruments_df() -> List[pd.DataFrame]:
    dir_all_files: List[str] = os.listdir(DATA_DICTIONARY_DIR)
    csv_files = [file for file in dir_all_files if '.csv' in file]
    instrument_dfs = [
            pd.read_csv(f'{DATA_DICTIONARY_DIR}/{file}') for file in csv_files
            ]
    return instrument_dfs


def upload_data_dictionary():
    config = load_config()
    data = pd.read_csv(DATA_DICTIONARY_FILE_PATH)
    redcap_url = 'https://redcap.miami.edu/api/'

    project_name = "Med IT Test project"
    request_data = {
            'token': config['test_token'],
            'content': 'metadata',
            'format': 'json',
            'data': data.to_json(orient='records'),
            'returnFormat': 'json'
            }

    print(f"Attempting to upload the data dictionary to {project_name}...")
    response = requests.post(redcap_url, request_data)
    print(response.text)
