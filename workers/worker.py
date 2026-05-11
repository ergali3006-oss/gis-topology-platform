from celery import Celery

celery_app = Celery(
    "topology_worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",
)


@celery_app.task
def ping() -> str:
    return "pong"
