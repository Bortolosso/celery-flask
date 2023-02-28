import time

from flask import jsonify

from project.server.celery import celery
from project.server.smartsheet.controller import return_controller


# Below are test processing workers.
@celery.task(
    name="create_task_get_all_sheets",
    queue="create_task",
    routing_key="task.create_task",
)
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return "TESTE"


@celery.task
def add(x, y):
    z = x + y
    print(z)


# Below are the daughters of Smartsheet data processing workers.
@celery.task(
    name="smartsheet_get_all_sheets",
    queue="get_all_sheets",
    routing_key="task.sheet.get.all",
)
def get_all_sheets():
    _proccess = return_controller()
    print(_proccess)
    return "TESTE"


# @celery.task(name="smartsheet_get_sheets", queue='get_sheets', routing_key='task.sheet')
# def init_sheet():
#     teste = get_data()
#     print(teste)
#     return ("TESTE")
