
# Import libraries
from datetime import timedelta

# Create the DAG instance
from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


# Create the DAG arguments
dag_arguments = {
    'owner': 'Laurindo benjamim',
    'start_date': days_ago(0),
    'email': ['rocketmc2009@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(days=1)
}

# Create the DAG instance
dag = DAG(
    dag_id = 'dag_process_web_log',
    default_args = dag_arguments,
    description = "Data Pipeline with Airflow",
    schedule_interval=timedelta(minutes=1)
)

extract_data = BashOperator(
    task_id="extract_ipadress_from_txt_file",
    bash_command="cut -f1 -d'-' airflow/dags/capstone/accesslog.txt > airflow/dags/capstone/extracted_data.txt",
    dag=dag
)

# Define and execute the data pipeline
extract_data

