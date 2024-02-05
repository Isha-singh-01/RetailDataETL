#!/usr/bin/env python
import pandas as pd
import requests
import json
import psycopg2
import psycopg2.extras as extras

import os
def extract():
    # ## Extract
    CUR_DIR = os.path.abspath(os.path.dirname(__file__))
    df = pd.read_csv(str(CUR_DIR)+'/Online_Retail.csv')
    return df 
    
# ## Transform
# Clean data for uploading
import os

def convert_columns(df):
    df.rename(
        columns={"InvoiceNo": "Invoice Number","InvoiceDate":"Invoice Date","CustomerID":"Customer ID"},
        inplace=True)
    df['Sales'] = df['UnitPrice']*df['Quantity']
    df = df.drop( columns=['No'])
    df.fillna(0,inplace=True)
    return df

# ## Load
# Load data into Postgres database

def create_table(conn):
    cur = conn.cursor() 
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS public.sales(
            id SERIAL PRIMARY KEY,
            "Invoice Number" VARCHAR(20),
            StockCode VARCHAR(20),
            Description VARCHAR(255),
            Quantity INTEGER,
            "Invoice Date" TIMESTAMP,
            UnitPrice REAL,
            "Customer ID" INTEGER,
            Country VARCHAR(100),
            Sales REAL);
        """)
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error) 
        conn.rollback()
    else:
        conn.commit()

def insert_values(conn, df, table):
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns)) 
    query = """INSERT INTO %s(%s) VALUES %%s;""" % (table, cols) 
    cursor = conn.cursor() 
    try: 
        extras.execute_values(cursor, query, tuples) 
        conn.commit() 
    except (Exception, psycopg2.DatabaseError) as error: 
        print("Error: %s" % error) 
        conn.rollback() 
        cursor.close() 
        return 1
    cursor.close()

def main():
    conn = psycopg2.connect(
        host="postgres", # changed from 'localhost' so it would work with docker
        database="retailsales",
        user="postgres", #your postgres username
        password="postgres")
    
    data = extract()
    print("Transforming...")
    create_table(conn)
    data = convert_columns(data)
    print("Loading...")
    insert_values(conn, data, 'sales')
    print("Finished.")

if __name__ == "__main__":
    main()