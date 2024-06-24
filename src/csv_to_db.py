## Dataset is dozens of .csv files.  This pulls them into an sql db for manipulation

import pandas as pd
from sqlalchemy import create_engine
import psycopg2 as pg2
import os
import glob
from dotenv import load_dotenv
from sqlalchemy import create_engine

## Pulls connection data from your .env file
load_dotenv()

dbname = os.getenv('F1DBNAME')
user = os.getenv('F1USER')
password = os.getenv('F1PASS')
host = os.getenv('F1HOST')
port = os.getenv('F1PORT')

# creates connectiont to your database

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

conn = engine.connect()

#pushes input file to your db

def csv_to_db(file_path,table_name):
    pd.read_csv(file_path, low_memory=False).to_sql(name = table_name, con=conn, if_exists="replace")


# Two arguments are file location and desired name.
python csv to db('data/race_data/TelemetryData_2048465535648368309.csv', 'TelemetryData_204' )

conn.close()