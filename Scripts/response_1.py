import pandas as pd
import numpy as np
from pathlib import Path
from azure.storage.blob import BlockBlobService
from io import StringIO
import datetime
import plotly.express as px
import json
from itertools import chain
from plotly.io import to_json

sas_token = '?sv=2021-04-10&st=2022-12-22T08%3A12%3A47Z&se=2023-12-30T08%3A12%3A00Z&sr=c&sp=racwl&sig=fMeYkXsCvwK%2F0qVrCmj2j3NiMricQjOPWOkAEXekIPA%3D'
account_name = 'willbedeletedsoon'
container_name = 'codx-pede-s02'
blob_name = 'wine_I0896.csv'
def get_data_from_blob(sas_token, account_name, container_name, blob_name):
    block_blob_service = BlockBlobService(account_name=account_name, sas_token= sas_token)
    from_blob = block_blob_service.get_blob_to_text(container_name = container_name, blob_name=blob_name)
    return pd.read_csv(StringIO(from_blob.content))
df_blob = get_data_from_blob(sas_token, account_name, container_name, blob_name)

def getTable(df, show_searchbar=False, multiple_tables=False):

    comp_dict = {}
    comp_dict['table_headers'] = df.columns.values.tolist()
    comp_dict['table_data'] = df.values.tolist()
    comp_dict['show_searchbar'] = show_searchbar
    comp_dict['multiple_tables'] = multiple_tables
    return comp_dict

container_dictionary = {}
container_dictionary = getTable(df_blob, show_searchbar = True)
container_dictionary

outputs_dict = json.dumps(container_dictionary)
