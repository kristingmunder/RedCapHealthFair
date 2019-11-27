import os
import csv
import json
import requests
import pandas as pd

from typing import List, Dict, TextIO, cast

full_file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(full_file_path)

CONFIG_FILE_PATH = f'{dir_name}/../config.json'
DATA_DICTIONARY_DIR = f'{dir_name}/../data'
DATA_DICTIONARY_FILE_PATH = f'{DATA_DICTIONARY_DIR}/DataDictionary.csv'


def load_config() -> dict:
    if 'TRAVIS' in os.environ and os.environ['TRAVIS'] == 'true':
        return cast(dict, os.environ)

    print("Loading Configuration file...")
    with open(CONFIG_FILE_PATH, 'r') as config_file:
        config_text: str = config_file.read()

    config: dict = json.loads(config_text)
    return config


def check_data_dir(data_dir=DATA_DICTIONARY_DIR):
    if os.path.exists(data_dir):
        return

    os.makedirs(data_dir)


def request_data_dictionary(main=False) -> requests.Response:
    """Request the data dictionary from the REDCap API"""
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
    return response


def download_json_data(main=False) -> str:
    res: requests.Response = request_data_dictionary(main)
    return res.text


def download_data_df(main=False) -> pd.DataFrame:
    """This downloads the data dictionary to a dataframe"""
    temp_file: str = './temp.csv'
    json_text: str = download_json_data(main)
    result: pd.DataFrame = json_to_csv(json_text, temp_file)
    os.remove(temp_file)
    return result


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
        keys: List[str] = list(json_data[0].keys())
        writer.writerow(keys)
        for entry in json_data:
            values: List[str] = [entry[x] for x in entry]
            writer.writerow(values)

    pd_data = pd.read_csv(csv_name)

    return pd_data


def upload_data_df(
        data_dictionary: pd.DataFrame,
        force_test: bool = False) -> requests.Response:
    config = load_config()
    redcap_url = 'https://redcap.miami.edu/api/'

    master: bool = 'master' in config.keys()
    cfg_test: str = config['test_token']
    cfg_main: str = config['main_token']
    project_name = "Med IT Test Project" if not master else "New REDCap"
    if force_test:
        project_token = cfg_test
    else:
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


def split_instrument_dataframe(df: pd.DataFrame) -> List[str]:
    instrument_list: List[str] = list(df['form_name'].unique())
    return [df[df['form_name'] == x] for x in instrument_list]


def save_instrument_lists(
        instruments: List[pd.DataFrame],
        directory: str = DATA_DICTIONARY_DIR):
    """Take our instruments and save them as csv"""
    check_data_dir(directory)
    ext: str = 'json'  # 'csv'

    # Save our order.json
    instrument_order: List[str] = [
            x['form_name'].iloc[0] for x in instruments
            ]
    with open(f'{directory}/order.json', 'w') as jo:
        json.dump(instrument_order, fp=jo, indent=4)

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


def read_json_instrument_df(json_file: str) -> pd.DataFrame:
    file_path: str = './temp.csv'
    with open(json_file, 'r') as json_fp:
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
    order_file: str = f'{dir}/order.json'
    with open(order_file, 'r') as fp_order:
        order: List[str] = json.load(fp_order)
    json_files = [
            f'{file_name}{ext}' for file_name in order
            ]

    instrument_dfs = [
            read_json_instrument_df(f'{dir}/{file}') for file in json_files
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
