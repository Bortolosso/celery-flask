# project/server/main/views.py

from celery.result import AsyncResult
from flask import render_template, jsonify, request

from project.server.blueprint import main_blueprint
from project.server.tasks import create_task, get_all_sheets


# Routes for tests
@main_blueprint.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")


@main_blueprint.route("/tasks", methods=["POST"])
def run_task():
    content = request.json
    task_type = content["type"]
    task = create_task.delay(int(task_type))
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


# Route o run workes SmartSheet
@main_blueprint.route("/smartsheet/get-all-sheets", methods=["POST"])
def smartsheet_get_all_sheets():
    content = request.json

    # task_ = get_all_sheets.delay()
    task_ = get_all_sheets()

    return jsonify({"task_id": "task_"}), 202
