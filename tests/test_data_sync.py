"""
test lib

This file tests all the functions in the lib.py file

Created by Kevin Davis
"""

import os
import json
import pandas as pd
import scripts.DataSync as DataSync

full_file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(full_file_path)


def test_load_config():
    config = DataSync.load_config()
    config_keys = list(config.keys())
    assert "main_token" in config_keys
    assert "test_token" in config_keys


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

    assert expected.equals(output)


def test_download_data_df():

    expected = type(pd.DataFrame())
    observed = type(DataSync.download_data_df())

    assert expected == observed
