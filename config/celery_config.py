import os

from kombu import Queue


def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "celery"}


class BaseConfig:
    broker_url: str = os.environ.get("broker_url", "amqp://guest:guest@localhost:5672//")
    result_backend: str = os.environ.get("result_backend", "rpc://")

    task_queues: list = [
        # default queue
        Queue("celery"),
        # custom queue
        Queue("recipes"),
    ]

    task_routes = (route_task,)


class DevelopmentConfig(BaseConfig):
    pass
