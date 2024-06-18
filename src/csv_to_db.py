## Dataset is dozens of .csv files.  This pulls them into an sql db for manipulation

import pandas as pd
from sqlalchemy import create_engine
import psycopg2 as pg2
import os
import glob
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

dbname = os.getenv('F1DBNAME')
user = os.getenv('F1USER')
password = os.getenv('F1PASS')
host = os.getenv('F1HOST')
port = os.getenv('F1PORT')



engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

conn = engine.connect()

#for fname in glob.glob('data/race_data/*.csv'):
pd.read_csv('data/race_data/TelemetryData_2048465535648368309.csv', low_memory=False).to_sql(name = 'TelemetryData_204', con=conn, if_exists="replace")

conn.close()