"""
test lib

This file tests all the functions in the lib.py file

Created by Kevin Davis
"""

import os
import json
import shutil
import pandas as pd
import scripts.DataSync as DataSync
from typing import List, Any

full_file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(full_file_path)

DATA_DICTIONARY_TEST_DIR = f'{DataSync.DATA_DICTIONARY_DIR}-test'


def test_load_config():
    config = DataSync.load_config()
    config_keys = list(config.keys())
    assert "main_token" in config_keys
    assert "test_token" in config_keys


def test_check_data_dir():
    if os.path.isdir(DATA_DICTIONARY_TEST_DIR):
        shutil.rmtree(DATA_DICTIONARY_TEST_DIR)

    DataSync.check_data_dir(DATA_DICTIONARY_TEST_DIR)

    assert os.path.isdir(DATA_DICTIONARY_TEST_DIR)


def test_json_to_cvs():

    input = [{
        "firstname": "Adam",
        "lastname": "Johnson"
    }, {
        "firstname": "Bob",
        "lastname": "Smith"
    }]

    json_input = json.dumps(input)
    print(json_input)

    file = f'{dir_name}/temp.csv'
    output = DataSync.json_to_csv(json_input, file_name=file)
    expected = pd.DataFrame(input)

    os.remove(file)
    assert expected.equals(output)


def test_download_data_df():

    expected = type(pd.DataFrame())
    observed = type(DataSync.download_data_df())

    assert expected == observed


def test_split_instrument_dataframe():

    temp_list: List[Any] = []
    df = DataSync.download_data_df()
    instrument_list = DataSync.split_instrument_dataframe(df)
    expected = type(temp_list)
    observed = type(instrument_list)
    assert observed == expected


def test_save_instrument_list():
    dir: str = DATA_DICTIONARY_TEST_DIR
    ext: str = '.json'

    df = DataSync.download_data_df()
    list_df = DataSync.split_instrument_dataframe(df)
    DataSync.save_instrument_lists(list_df, dir)

    dir_all_files: List[str] = os.listdir(dir)
    dir_files: List[str] = [
            file for file in dir_all_files
            if os.path.isfile(os.path.join(dir, file))]
    dir_csv_files: List[str] = [
            file for file in dir_files
            if ext in file
            ]

    expected: int = len(list_df)
    observed: int = len(dir_csv_files)

    assert expected == observed


def test_read_json_instrument_df():
    dir: str = DATA_DICTIONARY_TEST_DIR
    file: str = "vitals.json"

    with open(f'{dir}/{file}', 'r') as fp:
        json_data = json.load(fp)

    first_variable = json_data[0]
    keys: List[str] = list(first_variable.keys())
    first_key: str = keys[0]

    instrument_json: pd.DataFrame = DataSync.read_json_instrument_df(
            f'{dir}/{file}')
    first_column_name: str = instrument_json.columns.to_list()[0]

    assert first_column_name == first_key


def test_read_json_instruments_df():
    dir: str = DATA_DICTIONARY_TEST_DIR
    ext: str = '.json'

    n_csv_files: int = len([
        file for file in os.listdir(dir)
        if ext in file
            ])

    expected: int = n_csv_files
    observed: int = len(DataSync.read_json_instruments_df(dir))
    assert expected == observed


def test_compile_instrument_dataframe():
    dir: str = DATA_DICTIONARY_TEST_DIR
    num_entries: int = sum([
        instrument_df.shape[0]
        for instrument_df in DataSync.read_json_instruments_df(dir)
        ])

    instrument_dfs: List[pd.DataFrame] = DataSync.read_json_instruments_df(dir)
    data_dictionary: pd.DataFrame = DataSync.compile_instrument_dataframes(
            instrument_dfs
            )

    assert data_dictionary.shape[0] == num_entries


# Probably should create a test suite for this
def test_end():
    shutil.rmtree(DATA_DICTIONARY_TEST_DIR)
