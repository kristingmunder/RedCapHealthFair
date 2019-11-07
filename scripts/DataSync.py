import os
import csv
import json
import requests
import pandas as pd

from typing import List, Dict, TextIO

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


def check_data_dir(data_dir=DATA_DICTIONARY_DIR):
    if os.path.exists(data_dir):
        return

    os.makedirs(data_dir)


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

    return pd_data


def upload_data_df(data_dictionary: pd.DataFrame) -> requests.Response:
    config = load_config()
    redcap_url = 'https://redcap.miami.edu/api/'

    master: bool = 'master' in config.keys()
    cfg_test: str = config['test_token']
    cfg_main: str = config['main_token']
    project_name = "Med IT Test Project" if not master else "New REDCap"
    project_token = cfg_test if not master else cfg_main
    request_data = {
            'token': project_token,
            'content': 'metadata',
            'format': 'json',
            'data': data_dictionary.to_json(orient='records'),
            'returnFormat': 'json'
            }

    print(f"Attempting to upload the data dictionary to the {project_name}...")
    response = requests.post(redcap_url, request_data)
    print(response.text)
    return response


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

    temp_file: str = './temp.csv'
    result: pd.DataFrame = json_to_csv(response.text, temp_file)
    os.remove(temp_file)
    return result


def split_instrument_dataframe(df: pd.DataFrame) -> list:
    instrument_list: list = list(set(df['form_name']))
    return [df[df['form_name'] == x] for x in instrument_list]


def save_instrument_lists(
        instruments: List[pd.DataFrame],
        directory: str = DATA_DICTIONARY_DIR):
    """Take our instruments and save them as csv"""
    check_data_dir(directory)
    ext: str = 'json'  # 'csv'
    for instrument_df in instruments:
        instrument_name: str = list(set(instrument_df['form_name']))[0]
        instrument_file: str = f'{directory}/{instrument_name}.{ext}'
        json_data = instrument_df.to_json(orient='records')
        dict: Dict = json.loads(json_data)
        json_data = json.dumps(dict, indent=4)
        filehandle: TextIO = open(instrument_file, 'w')
        filehandle.write(json_data)
        filehandle.close()
        # json_to_csv(json_data, instrument_csv_file)


def read_json_instrument_df(file: str) -> pd.DataFrame:
    file_path: str = './temp.csv'
    with open(file, 'r') as json_fp:
        json_object: Dict = json.load(json_fp)
        json_string: str = json.dumps(json_object)
    json_to_csv(json_string, file_path)
    instrument_df: pd.DataFrame = pd.read_csv(file_path)
    os.remove(file_path)
    return instrument_df


def read_json_instruments_df(
        dir: str = DATA_DICTIONARY_DIR
        ) -> List[pd.DataFrame]:
    ext: str = '.json'
    dir_all_files: List[str] = os.listdir(dir)
    csv_files = [file for file in dir_all_files if ext in file]
    instrument_dfs = [
            read_json_instrument_df(f'{dir}/{file}') for file in csv_files
            ]
    return instrument_dfs


def compile_instrument_dataframes(
        instrument_dataframes: List[pd.DataFrame]
        ) -> pd.DataFrame:
    data_dictionary: pd.DataFrame = instrument_dataframes[0]
    for instrument_dataframe in instrument_dataframes[1:]:
        data_dictionary = data_dictionary.append(
                instrument_dataframe,
                ignore_index=True
                )

    return data_dictionary
