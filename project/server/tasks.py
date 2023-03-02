import time

from flask import jsonify

from project.server.celery import celery
from project.server.smartsheet.add.controller import add_interable_db
from project.server.smartsheet.sheets.controller import init_get_all_sheets 
from project.server.smartsheet.syngentadirect.controller import init_get_sheet_syngenta_direct


# Below are test processing workers.
@celery.task(
    name="add",
    queue="add",
    routing_key="tasks.add",
)
def add(x, y):
    proccess_add = add_interable_db()
    return proccess_add

# Below are the daughters of Smartsheet data processing workers.
@celery.task(
    name="smartsheet_get_all_sheets",
    queue="get_all_sheets",
    routing_key="tasks.sheets.get_all_sheets",
)
def get_all_sheets():
    proccess_sheets = init_get_all_sheets()
    return proccess_sheets


@celery.task(
    name="smartsheet_get_sheet_syngenta_direct",
    queue="get_sheet_syngenta_direct",
    routing_key="tasks.sheet.syngenta.direct",
)
def get_sheet_syngenta_direct():
    proccess_syngenta_direct = init_get_sheet_syngenta_direct()
    return proccess_syngenta_direct
