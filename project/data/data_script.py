import pandas as pd
import os.path
from urllib.parse import urlparse


def read_cycling_data():
    locations = {"100035541": "Neutor"}
    location = "100035541"
    year = "2020"
    month = "04"

    query_url = f"https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/{location}/{year}-{month}.csv"

    df = pd.read_csv(query_url)
    
    # 30/31 days * 24 hours * 4 15-min intervals
    print(len(df), "entries") 
    
    return df

def read_rain_data():
    stations = {"01766": "Münster/Osnabrück"}
    station = "01766"
    
    file_path = f"./produkt_zehn_min_rr_20200101_20221231_{station}.txt"
    df = pd.read_csv(file_path, delimiter=";")
    
    # 3 years * 365 days * 24 hours * 6 10-min intervals + 1 leap day * 24 * 6
    print(len(df), "entries")
    
    # convert time into correct format
    df["MESS_DATUM"] = pd.to_datetime(df["MESS_DATUM"], format="%Y%m%d%H%M")
    
    return df

df_cycling = read_cycling_data()
df_rain = read_rain_data()    
print(df_cycling.head())
#print(df_rain["RWS_10"].value_counts())
