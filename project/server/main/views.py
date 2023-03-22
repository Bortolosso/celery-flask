# project/server/main/views.py

from celery.result import AsyncResult
from flask import render_template, jsonify, request

from project.server.blueprint import main_blueprint
from project.server.tasks import (
    add,
    get_all_sheets,
    get_sheet_syngenta_direct_greenfield,
    get_salesforce_contact,
    get_sheet_syngenta_direct_approved_leads,
)


# Routes for tests
@main_blueprint.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")


@main_blueprint.route("/add", methods=["POST"])
def run_task():
    content = request.json
    task_type = content["type"]

    task = add(1, 1)

    return jsonify({"task_id": task.id}), 202


@main_blueprint.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return jsonify(result), 200


#### Route run workes SmartSheet


@main_blueprint.route("/smartsheet/sheets", methods=["POST"])
def smartsheet_get_all_sheets():
    content = request.json
    task_ = get_all_sheets()

    return jsonify({"task_id": "get_all_sheets"}), 202


@main_blueprint.route("/smartsheet/sheet-syngenta-direct-greenfield", methods=["POST"])
def smartsheet_get_sheet_syngenta_direct_greenfield():
    content = request.json
    task_ = get_sheet_syngenta_direct_greenfield.delay()

    return jsonify({"task_id": "get_sheet_syngenta_dinamic_greenfield"}), 202


@main_blueprint.route(
    "/smartsheet/sheet-syngenta-direct/approved-leads", methods=["POST"]
)
def smartsheet_get_sheet_syngenta_direct_approved_leads():
    content = request.json
    task_ = get_sheet_syngenta_direct_approved_leads()

    return jsonify({"task_id": "get_sheet_syngenta_direct_approved_leads"}), 202


### Routes run workers Salesforce
@main_blueprint.route("/salesforce/contact", methods=["POST"])
def salesforce_get_contact():
    content = request.json
    task_ = get_salesforce_contact.delay()

    return jsonify({"task_id": "get_salesforce_contact"}), 202
