from airflow import DAG
from airflow import configuration as conf
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

default_args = { 'owner': 'lattechiffon', 'start_date': datetime(2022, 1, 31)}
dag = DAG('test-dag', schedule_interval='@once', default_args=default_args)

##############################
k_2 = KubernetesPodOperator(
    task_id='root-test-task',
    name='test-hello-world',
    namespace='airflow',
    image='hello-world:latest',
    in_cluster=True,
    config_file=None,
    is_delete_operator_pod=False,
    get_logs=True, 
    dag=dag
)
