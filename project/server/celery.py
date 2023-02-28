from celery import Celery

celery = Celery('tasks')
celery.config_from_object('project.server.celeryconfig', False, True)