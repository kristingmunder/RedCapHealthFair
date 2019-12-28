"""
This file will actually test your data upload to ensure that you data
dictionary edits cause any problems
"""

import requests
import pandas as pd
import scripts.DataSync as ds

from typing import List


def test_upload():

    # Obtain our data dictionary
    instrument_dfs: List[pd.DataFrame] = ds.read_json_instruments_df()
    data_dictionary: pd.DataFrame = ds.compile_instrument_dataframes(
            instrument_dfs
            )
    response: requests.Response = ds.upload_data_df(data_dictionary)

    assert response.status_code == 200
