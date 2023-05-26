import pandas as pd
from sqlalchemy import create_engine
import requests, zipfile
from io import BytesIO


def download_rain_data(location):
    print('Downloading started')
    # Defining the zip file URL
    url = f'https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/precipitation/historical/10minutenwerte_nieder_{location}_20200101_20221231_hist.zip'

    # Split URL to get the file name
    filename = url.split('/')[-1]

    # Downloading the file by sending the request to the URL
    req = requests.get(url)
    print('Downloading Completed')

    # extracting the zip file contents
    zip_file= zipfile.ZipFile(BytesIO(req.content))
    zip_file.extractall('./data/rain')


def read_rain_data(station):
        
    file_path = f"./data/rain/produkt_zehn_min_rr_20200101_20221231_{station}.txt"
    df = pd.read_csv(file_path, delimiter=";")
    
    # 3 years * 365 days * 24 hours * 6 10-min intervals + 1 leap day * 24 * 6
    #print(len(df), "entries")
    
    # convert time into correct format
    df["MESS_DATUM"] = pd.to_datetime(df["MESS_DATUM"], format="%Y%m%d%H%M")
         
    return df


def read_cycling_data(location, time_frame):
    
    df = pd.DataFrame()
    for element in time_frame:
        year = str(element.year)
        month = str(element.month).zfill(2)
        query_url = f"https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/{location}/{year}-{month}.csv"

        df_month = pd.read_csv(query_url)
        
        df = pd.concat([df, df_month])
        
    # 3 years * 365 days * 24 hours * 4 15-min intervals + 1 leap day * 24 * 4
    # entries missing
    #print(len(df), "entries") 
    
    return df


def write_data_to_sql(data, table_name):
    engine = create_engine('sqlite:///data/my_data.sqlite', echo=False)
    data.to_sql(table_name, con=engine, if_exists='replace', index=False)


def gather_data():
    cycling_locations = {"100035541": "Neutor"}
    cycling_location = "100035541"

    rain_locations = {"01766": "Münster/Osnabrück"}
    rain_location = "01766"
    
    time_frame = pd.Series(pd.date_range("2020-01-01", "2022-12-31", freq="M"))

    download_rain_data(rain_location)
    
    df_rain = read_rain_data(rain_location)    
    df_cycling = read_cycling_data(cycling_location, time_frame)

    write_data_to_sql(df_rain, "rain")
    write_data_to_sql(df_cycling, "cycling")
    