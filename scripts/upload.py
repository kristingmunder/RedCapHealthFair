"""
This file is for editors to load thier currently saved json files into the Med
IT test project to begin editing
"""

import scripts.DataSync as ds

instruments = ds.read_json_instruments_df()
data_dictionary = ds.compile_instrument_dataframes(instruments)
ds.upload_data_df(data_dictionary, force_test=True)
