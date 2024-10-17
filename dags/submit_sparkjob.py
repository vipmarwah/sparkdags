from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'submit_spark_application',
    default_args=default_args,
    schedule_interval=None,
)

k8s_task = KubernetesPodOperator(
        namespace='default',  # Kubernetes namespace
        image="python:3.8-slim",  # Docker image to use
        cmds=["python", "-c"],
        arguments=[
            "print('Hello from Kubernetes Pod Operator!')"
        ],
        labels={"foo": "bar"},  # Optional labels
        name="airflow-test-pod",  # Name of the pod
        task_id="run_pod",
        get_logs=True,  # Capture pod logs and display in Airflow
        is_delete_operator_pod=True,  # Delete pod after task completion
        in_cluster=True,  # Run within the cluster
        do_xcom_push=False,  # Disable XCom if not needed
    )
# submit_spark_app = KubernetesPodOperator(
#     namespace='default',
#     name="submit-spark-job",
#     task_id="submit-spark-app",
#     is_delete_operator_pod=True,
#     in_cluster=True,
#     dag=dag,
#     cmds=["kubectl", "apply", "-f", "https://github.com/vipmarwah/sparkdags/sparkapp.yaml"],
#     image="bitnami/kubectl:latest",
#     #get_logs=True,
# )

k8s_task