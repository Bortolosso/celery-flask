import time

from flask import jsonify

from project.server.celery import celery
from project.server.smartsheet.add.controller import add_interable_db
from project.server.smartsheet.sheets.controller import init_get_all_sheets
from project.server.smartsheet.syngentadirect.greenfield.controller import (
    init_get_sheet_syngenta_direct_greenfield,
)
from project.server.smartsheet.syngentadirect.approvedleads.controller import (
    init_get_sheet_syngenta_direct_approved_leads,
)

from project.server.salesforce.controller import init_request_contact_sales_force


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
    max_retries=3,
)
def get_all_sheets():
    proccess_sheets = init_get_all_sheets()
    return proccess_sheets


@celery.task(
    name="smartsheet_get_sheet_syngenta_direct_greenfield",
    queue="get_sheet_syngenta_direct_greenfield",
    routing_key="tasks.sheet.syngenta.direct.greenfield",
)
def get_sheet_syngenta_direct_greenfield():
    proccess_syngenta_direct_greenfield = init_get_sheet_syngenta_direct_greenfield()
    return proccess_syngenta_direct_greenfield


@celery.task(
    name="smartsheet_get_sheet_syngenta_direct_approved_leads",
    queue="get_sheet_syngenta_direct_approved_leads",
    routing_key="tasks.sheet.syngenta.direct.approved.leads",
)
def get_sheet_syngenta_direct_approved_leads():
    proccess_syngenta_direct = init_get_sheet_syngenta_direct_approved_leads()
    return proccess_syngenta_direct


# Below are the daughters of Salesforce data processing workers.
@celery.task(
    name="salesforce_get_contacts",
    queue="test_contact_salesforce",
    routing_key="tasks.sales.contact",
)
def get_salesforce_contact():
    proccess_contact = init_request_contact_sales_force()
    return proccess_contact
