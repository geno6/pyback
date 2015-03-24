from huey.djhuey import task
import logging

@task()
def count_beans():
    logger = logging.getLogger(__name__)
    logger.debug("HUEEEEY")