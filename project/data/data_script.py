import pandas as pd
from sqlalchemy import create_engine


def read_cycling_data():
    locations = {"100035541": "Neutor"}
    location = "100035541"
    year = "2020"
    month = "04"

    query_url = f"https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/{location}/{year}-{month}.csv"

    df = pd.read_csv(query_url)
    
    # 30/31 days * 24 hours * 4 15-min intervals
    #print(len(df), "entries") 
    
    return df

def read_rain_data():
    stations = {"01766": "Münster/Osnabrück"}
    station = "01766"
    
    # Download from https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/precipitation/historical/
    # unpack and store .txt in /data folder
    file_path = f"./produkt_zehn_min_rr_20200101_20221231_{station}.txt"
    df = pd.read_csv(file_path, delimiter=";")
    
    # 3 years * 365 days * 24 hours * 6 10-min intervals + 1 leap day * 24 * 6
    #print(len(df), "entries")
    
    # convert time into correct format
    df["MESS_DATUM"] = pd.to_datetime(df["MESS_DATUM"], format="%Y%m%d%H%M")
    
    return df

def write_data_to_sql(data, table_name):
    engine = create_engine('sqlite:///my_data.sqlite', echo=False)
    data.to_sql(table_name, con=engine, if_exists='replace')
    
df_cycling = read_cycling_data()
df_rain = read_rain_data()    

write_data_to_sql(df_cycling, "cycling")
write_data_to_sql(df_rain, "rain")
