import pandas as pd
import os
from sqlalchemy import create_engine # sqlalchemy is a python library and create_engine is a function to used connect the database with python
import logging # its a build-in module
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'
)
engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''this function will ingest the dataframe into databse table'''
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)

def load_raw_data():
    '''this function will load data the csv as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if ".csv" in file:
            df = pd.read_csv("data/"+file) # data access with path and full file
            logging.info (f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end =  time.time()
    total_time = (end - start)/60
    logging.info('---------------------Ingestion Complete--------------------')

    logging.info(f"\nTotal Time Taken: {total_time} minutes")

if __name__ == '__main__':
    load_raw_data()