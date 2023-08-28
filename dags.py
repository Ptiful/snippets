rom datetime import timedelta
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
import os

default_args = {
    'owner': 'maxim',
    'depends_on_past': False,
    'email': ['maxim@becode.org'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}



# List of scrapers that have been converted into Docker images
scraper_names = [
    "demorgen",
    "dhnet",
    "hln",
    "knack",
    "lalibre",
    "lavenir",
    "lecho",
    "lesoir",
    "levif_actuality",
    "levif_news",
    "levif_trends",
    "rtbf",
    "sudinfo",
    "tijd",
    "vrt",
]

with DAG('scraping_pipeline',
    default_args=default_args,
    schedule_interval='@hourly',  # Run every day at midnight
    start_date=days_ago(1),
) as dag:

    scraper_tasks = []
    # Create a DockerOperator task for each scraper image
    for scraper_name in scraper_names:
        image_name = f"graphtylove/datatank_scraper_{scraper_name}"
        
        task = DockerOperator(
            docker_url='tcp://docker-proxy:2375',
            image=image_name,
            network_mode='bridge',
            task_id=f"task___scraper_{scraper_name}",
            force_pull=True,
            auto_remove=True,
            environment={
                "MONGODB_URI": "{{ var.value.mongodb_uri }}",
            }
        )
        scraper_tasks.append(task)

    # Dummy task as a synchronization point
    sync_task = DummyOperator(task_id='task___sync_task')

    # Task for the preprocessing step
    preprocessing_task = DockerOperator(
        docker_url='tcp://docker-proxy:2375',
        image='graphtylove/datatank_data_preprocessing',
        network_mode='bridge',
        task_id='task___preprocessing',
        force_pull=True,
        auto_remove=True,
        environment={
            "MONGODB_URI": "{{ var.value.mongodb_uri }}",
        }
    )

    # Setting up the pipeline run order
    for scraper_task in scraper_tasks:
       scraper_task >> sync_task

    sync_task >> preprocessing_task