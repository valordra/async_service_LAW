from fastapi import APIRouter
from starlette.responses import JSONResponse

from api import recipes
from celery_tasks.tasks import get_recipes_by_query_task
from config.celery_utils import get_task_info
from schemas.schemas import RecipeQuery

router = APIRouter(prefix='/recipes', tags=['Recipes'], responses={404: {"description": "Not found"}})


@router.post("/")
def get_recipes_by_query(recipe_query: RecipeQuery) -> dict:
    """
    Return a List of recipes by the query or foodname e.g "hamburger"/"pasta" provided
    in input in a sync way
    """
    data: dict = {}
    data.update(recipes.get_recipes_by_query(recipe_query.query))
    return data


@router.post("/async")
async def get_recipes_by_query_async(recipe_query: RecipeQuery):
    """
    Return a List of recipes by the query or foodname e.g "hamburger"/"pasta" provided
    in input in an async way. The task id will be returned, which can later be used to get the result.
    """
    task = get_recipes_by_query_task.apply_async(args=[recipe_query.query])
    return JSONResponse({"task_id": task.id})


@router.get("/task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Return the status of the submitted Task
    """
    return get_task_info(task_id)

