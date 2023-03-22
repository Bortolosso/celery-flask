from celery.schedules import crontab

import os


broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "America/Sao_Paulo"
enable_utc = True
task_default_exchange = "default"
task_default_exchange_type = "topic"
task_default_routing_key = "tasks.default"
task_default_queue = "default"

beat_schedule = {
    # "test-add": {
    #     "task": "add",
    #     "schedule": crontab(minute="*/5"),
    #     "args": (1, 1),
    #     # 'options': {
    #     #    'expires': 15.0,
    #     # },
    # },
    # "test-end-to-end-insert-table": {
    #     "task": "smartsheet_get_all_sheets",
    #     "schedule": crontab(),
    #     "args": (),
    #     # 'options': {
    #     #    'expires': 15.0,
    #     # },
    # },
    "smartsheet-syngenta-direct": {
        "task": "smartsheet_get_sheet_syngenta_direct_greenfield",
        "schedule": crontab(minute='*/30'),
        "args": (),
        # 'options': {
        #    'expires': 15.0,
        # },
    },
}
