import pandas as pd
import zipfile
import urllib.request
from sqlalchemy import create_engine


# fetching the zip file
zip_url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
filename = "./exercises/mowesta.zip"    
urllib.request.urlretrieve(zip_url, filename)

# extracting zip file
zip_file= zipfile.ZipFile(filename)
zip_file.extractall('./exercises')

# reading in the csv file
df = pd.read_csv("./exercises/data.csv", sep=";", decimal=",", index_col=False, 
                 usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"])

# renaming columns
df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

# transforming data
df["Temperatur"] = df["Temperatur"] * 9/5 + 32
df["Batterietemperatur"] = df["Batterietemperatur"] * 9/5 + 32

# validate data
df = df[(df["Geraet"] > 0) & 
        (df["Monat"] > 0) & 
        ((df["Geraet aktiv"]=="Ja") | 
         (df["Geraet aktiv"]=="Nein"))]

# write to sqlite database
engine = create_engine('sqlite:///./temperatures.sqlite', echo=False)
df.to_sql("temperatures", con=engine, if_exists='replace', index=False)
