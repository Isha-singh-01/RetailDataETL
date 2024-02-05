from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta

default_args = {
   'owner': 'airflow',
   'depends_on_past': False,
   'retries': 0
}

dag=DAG(
    dag_id='retailDAG',
    default_args=default_args,
    start_date=datetime(2024,2,4),
    catchup=False,
    schedule_interval='*/10 * * * *', #every 10 minutes
    )
    
t1 = BashOperator(
    task_id = 'Bash_task',
    bash_command = 'python $AIRFLOW_HOME/dags/scripts/etl.py',
    dag = dag
    )
    
t1
