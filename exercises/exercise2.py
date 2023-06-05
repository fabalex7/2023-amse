import re
import pandas as pd
from sqlalchemy import create_engine

# load csv from url
url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
df = pd.read_csv(url, sep=";", decimal=",")


# drop Status column
df = df.drop(columns=["Status"])

# remove rows with empty cells
df = df.dropna()

# assign dtype for column "Betreiber_Nr"
df["Betreiber_Nr"] = df["Betreiber_Nr"].astype(int)

# remove faulty values in column "Verkehr"
verkehr_values = ["FV", "RV", "nur DPN"]
df = df[df["Verkehr"].isin(verkehr_values)]

# remove values that are <-90 or >90 in columns "Laenge" and "Breite"
wrong_coordinates = df[(df["Laenge"] > 90) | (df["Laenge"] < -90) | (df["Breite"] > 90) | (df["Breite"] < -90)].index
df = df.drop(wrong_coordinates)

# remove values that don't fit the scheme for column "IFOPT"
df = df[df["IFOPT"].str.match(r'\w{2}:\d*:\d*(:\d*)?$')==True]

# write to sqlite database
engine = create_engine('sqlite:///./trainstops.sqlite', echo=False)
df.to_sql("trainstops", con=engine, if_exists='replace', index=False)
