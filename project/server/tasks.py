import time

from flask import jsonify

from project.server.celery import celery
from project.server.smartsheet.sheets.controller import init_get_all_sheets
from project.server.smartsheet.syngentadirect.controller import init_get_sheet_syngenta_direct


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


# Below are the daughters of Smartsheet data processing workers.
@celery.task(
    name="smartsheet_get_all_sheets",
    queue="get_all_sheets",
    routing_key="task.sheets.get.all",
)
def get_all_sheets():
    proccess_sheets = init_get_all_sheets()
    return "TESTE"


@celery.task(
    name="smartsheet_get_sheet_syngenta_direct",
    queue="get_sheet_syngenta_direct",
    routing_key="task.sheet.syngenta.direct",
)
def get_sheet_syngenta_direct():
    proccess_syngenta_direct = init_get_sheet_syngenta_direct()
    return "TESTE"
