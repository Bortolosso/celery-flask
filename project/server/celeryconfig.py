from kombu import Queue
from celery.schedules import crontab

import os


broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/Sao_Paulo'
enable_utc = True
task_default_exchange = "default"
task_default_exchange_type = "topic"
task_default_routing_key = "task.default"
task_default_queue = 'default'
task_routes = {
   'project.server.tasks.get_all_sheets': {
      'queue': 'get_all_sheets', 
      'routing_key': 'task.sheet.get.all'
   },
   'project.server.tasks.create_task': {
      'queue': 'create_task', 
      'routing_key': 'task.create_task'
   },
   'project.server.tasks.add': {
      'queue': 'add', 
      'routing_key': 'task.add'
   }
}
task_queues = (
   # Queue('default',    routing_key='task.create_task'),
   Queue('get_all_sheets', routing_key='task.sheet.get.all'),
   Queue('add', routing_key='task.add'),
)
beat_schedule = {
   'add-every-30-seconds': {
      'task': 'project.server.tasks.add',
      'schedule': crontab(),
      'args': (16, 16),
      # 'options': {
      #    'expires': 15.0,
      # },
   },
}