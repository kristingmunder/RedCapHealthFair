"""
If you prefer to make edits to the data dictionary and the instruments on
REDCaps designer, you can run the script to pull down the test project
instruments and update you current CSV files
"""

import pandas as pd
import DataSync as ds

from typing import List


data_dictionary_df: pd.DataFrame = ds.download_data_df(main=True)


instrument_dfs: List[pd.DataFrame] = ds.split_instrument_dataframe(
        data_dictionary_df
        )

ds.save_instrument_lists(instrument_dfs)
