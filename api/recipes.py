import json

import httpx

from schemas.schemas import Recipe

url = 'https://api.spoonacular.com/recipes/complexSearch'
food_api_key = "438b936648d74387a2e723ccfbdfbd0f"


def get_recipes_by_query(recipe_query: str) -> dict:
    print('get_recipes_by_query ', recipe_query)
    params = {'query': recipe_query,
              'apiKey': food_api_key}
    client = httpx.Client()
    response = client.get(url, params=params)
    response_json = json.loads(response.text)
    print(response_json)
    print(response_json["results"])
    recipes = []
    for recipe in response_json["results"]:
        recipe_obj = Recipe.parse_obj(recipe)
        recipes.append(recipe_obj)
    return {recipe_query: recipes}
