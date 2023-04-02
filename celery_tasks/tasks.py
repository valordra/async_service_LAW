from typing import List

from celery import shared_task

from api import recipes


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='recipes:get_recipes_by_query_task')
def get_recipes_by_query_task(self, query: str):
    data: dict = {}
    data.update(recipes.get_recipes_by_query(query))
    return data
