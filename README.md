# Retail Data Pipeline

This project aims to automate the extraction of data from a CSV file hosted in a remote repository, loading it into a PostgreSQL database, orchestrating the workflow using Apache Airflow, and finally creating a dashboard using Tableau for visualization.<br>

<img src="https://raw.githubusercontent.com/Isha-singh-01/RetailAnalyticsusingAWS/main/diagram.png" width=650>


## Project Structure

### Files

- **retailDAG.py**: This file defines an Airflow Directed Acyclic Graph (DAG) named 'retailDAG'. It orchestrates the workflow by defining tasks to be executed at specific intervals. In this DAG, there is a BashOperator task named 'Bash_task' that runs a Python script (`etl.py`) responsible for extracting, transforming, and loading the data.

- **etl.py**: This Python script contains functions to extract data from the CSV file, transform it by renaming columns, calculating sales, and cleaning the DataFrame, create a PostgreSQL table if it doesn't exist, and insert the transformed data into the PostgreSQL table. The main function establishes a connection to the PostgreSQL database, performs the ETL process, and closes the connection.

### ETL Process

- **Data Extraction**: The `extract()` function reads data from the CSV file (`Online_Retail.csv`) into a Pandas DataFrame.

- **Data Transformation**: The `convert_columns()` function renames columns, calculates sales, and cleans the DataFrame.

- **Data Loading**: The `create_table()` function creates a PostgreSQL table named 'sales' if it doesn't exist, and the `insert_values()` function inserts the transformed data into the table.

## Usage

1. Clone the repository to your local machine.
2. Set up Apache Airflow and Docker if not already installed.
3. Copy `retailDAG.py` and `etl.py` to your Airflow DAGs directory.
4. Configure Airflow to connect to your PostgreSQL database.
5. Start the Airflow scheduler and webserver.
6. Airflow will automatically execute the DAG according to the defined schedule, extracting data from the CSV file and loading it into the PostgreSQL database.

## Dashboard

After successfully loading the data into the PostgreSQL database,I created a dashboard using Tableau to provide various KPI's from retail dataset.
- Dashboard link: [here](https://public.tableau.com/views/RetailAnalytics_17071970683850/RetailAnalyticsDashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
