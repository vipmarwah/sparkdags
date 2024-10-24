from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
default_args = {
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'submit_spark_application',
    default_args=default_args,
    schedule_interval=None,
)

submit_spark_app = SparkSubmitOperator(
    task_id='submit_spark_job',
    application='https://github.com/vipmarwah/sparkdags/sparkapp.yaml',  # Path to your Spark job
    conn_id='airflow-spark', 
    env_vars={
            'JAVA_HOME': '/opt/java/openjdk/lib',  # Path to your Java installation
        },
    dag=dag,
    # namespace='sparkapplication',
    # name="submit-spark-job",
    # task_id="submit-spark-app",

    # is_delete_operator_pod=True,
    # in_cluster=True,
    # dag=dag,
    # cmds=["kubectl", "apply", "-f", "https://github.com/vipmarwah/sparkdags/sparkapp.yaml"],
    # image="bitnami/kubectl:latest",
    # get_logs=True,
)

submit_spark_app