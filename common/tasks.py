from celery import shared_task
from time import sleep


@shared_task(queue='simple_queue', ignore_result=True)
def my_task():
    sleep(10)
    print("task done")
    return "Done"
