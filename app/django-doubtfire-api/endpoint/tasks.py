from celery import shared_task

@shared_task
def test(param):
    return 'The test task executed with argument "%s" ' % param
