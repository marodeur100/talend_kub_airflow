from airflow.utils.dates import days_ago
from airflow.utils.log.logging_mixin import LoggingMixin
from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.contrib.kubernetes.volume_mount import VolumeMount  # noqa
from airflow.contrib.kubernetes.volume import Volume 

log = LoggingMixin().log

try:
    # Kubernetes is optional, so not available in vanilla Airflow
    # pip install apache-airflow[kubernetes]
    from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

    args = {
        'owner': 'airflow',
        'start_date': days_ago(2),
        'retries': 1,
        'retry_delay': timedelta(minutes=2)
    }

    dag = DAG(
        dag_id='talend_kubernetes_example',
        default_args=args,
        schedule_interval=None)

    tolerations = [
        {
            'key': "key",
            'operator': 'Equal',
            'value': 'value'
        }
    ]

    volume_out = VolumeMount('outpath',
                            mount_path='/opt/talend/out_files/',
                            sub_path=None,
                            read_only=False)

    volume_config= {
    'hostPath':
          {
            'path': '/home/osboxes/out/'
           }
        }
    volume1 = Volume(name='outpath', configs=volume_config)

    stgstate = KubernetesPodOperator(
        namespace='default',
        image="marodeur100/loadstatetostaging:0.1",
        env_vars={"ARGS": "--context_param csvfolder=/opt/talend/input_files/ --context_param postgres_Server=postgres-airflow --context_param postgres_Login=root --context_param postgres_Password=root --context_param postgres_Database=airflow --context_param postgres_Port=5432"},
        name="stgstate-pod",
        in_cluster=True,
        task_id="stgstate",
        get_logs=True,
        dag=dag,
        is_delete_operator_pod=False,
        tolerations=tolerations
    )

    stgcustomers = KubernetesPodOperator(
        namespace='default',
        image="marodeur100/loadcustomerstostaging:0.1",
        env_vars={"ARGS": "--context_param csvfolder=/opt/talend/input_files/ --context_param postgres_Server=postgres-airflow --context_param postgres_Login=root --context_param postgres_Password=root --context_param postgres_Database=airflow --context_param postgres_Port=5432"},
        name="stgcustomers-pod",
        in_cluster=True,
        task_id="stgcustomers",
        get_logs=True,
        dag=dag,
        is_delete_operator_pod=False,
        tolerations=tolerations
    )

    aggcustomers = KubernetesPodOperator(
        namespace='default',
        image="marodeur100/loadaggrcustomers:0.1",
        env_vars={"ARGS": "--context_param postgres_Server=postgres-airflow --context_param postgres_Login=root --context_param postgres_Password=root --context_param postgres_Database=airflow --context_param postgres_Port=5432"},
        name="aggcustomers-pod",
        in_cluster=True,
        task_id="aggcustomers",
        get_logs=True,
        dag=dag,
        is_delete_operator_pod=False,
        tolerations=tolerations
    )

    extractcustomers = KubernetesPodOperator(
        namespace='default',
        image="marodeur100/extractcustomernf:0.1",
        env_vars={"ARGS": "--context_param outfolder=/opt/talend/out_files/ --context_param postgres_Server=postgres-airflow --context_param postgres_Login=root --context_param postgres_Password=root --context_param postgres_Database=airflow --context_param postgres_Port=5432"},
        name="extractcustomers-pod",
        in_cluster=True,
        volumes=[volume1],
        volume_mounts=[volume_out],
	task_id="extractcustomers",
        get_logs=True,
        dag=dag,
        is_delete_operator_pod=False,
        tolerations=tolerations
    )

    # construct dependencies
    [stgstate, stgcustomers] >> aggcustomers >> extractcustomers
except ImportError as e:
    log.warn("Could not import KubernetesPodOperator: " + str(e))
    log.warn("Install kubernetes dependencies with: "
             "    pip install apache-airflow[kubernetes]")



