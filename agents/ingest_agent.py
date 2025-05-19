import pandas as pd
import requests
from io import StringIO

def ingest_csv_from_gdrive():
    file_id = "1zLuphyJJGJoXZBmAnPqW8_Lxqw42KYbC"
    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
    response = requests.get(download_url)
    df = pd.read_csv(StringIO(response.text))
    return df
