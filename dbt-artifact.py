from airflow import DAG
from airflow import models
# Make sure to add below
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'dummy',
    'retries': 0,
}

docker_dag = DAG(
    dag_id='dbt_docker_test',
    default_args=args,
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    tags=['dbt run model'],
)

quay_k8s = KubernetesPodOperator(
    # k8s namespace created earlier
    namespace='dbt-ns', 
    # k8s service account name created earlier
    service_account_name='dbt-composer-sa@mineral-anchor-361313.iam.gserviceaccount.com', 
    # Ensures that the right node-pool is used
    nodeSelector={'http://cloud.google.com/gke-nodepool': 'dbt-pool'}, 
    # Ensures that cache is always refreshed
    image_pull_policy='Always', 
    # Artifact image of dbt repo
    image='australia-southeast1-docker.pkg.dev/mineral-anchor-361313/my-dbt-repo/my-image', 
    # links to ENTRYPOINT in .sh file
    cmds=['/app/dbt_run.sh'], 
    # matches sequence of arguments in .sh file (mode,dbt_target,dbt_models,dbt_vars,full_refresh)
    arguments=['run', 'projectzone', 'tag:test2', '{from_date: "", to_date: ""}','False'], 
    name="run-dbt-in-pod",
    task_id="run-dbt-in-pod",
    get_logs=True,
    dag=docker_dag,    
    )