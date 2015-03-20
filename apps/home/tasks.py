import logging

from celery.task import task

@task
def home_task():
    logger = logging.getLogger(__name__)
    logger.error("Hello from logger!")