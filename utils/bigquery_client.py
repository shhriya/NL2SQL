import os
from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()
client = bigquery.Client() #it is a job ,lets you send SQL queries, fetch datasets, create tables, etc.

def run_query(sql: str):
    job = client.query(sql)  #will execute but will not give any result
    result = job.result()   # gives the actual result
    return [dict(row) for row in result]
