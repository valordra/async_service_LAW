from typing import List, Optional

from pydantic import BaseModel


class RecipeQuery(BaseModel):
    query: str

    class Config:
        schema_extra = {
            "example": {
                "query": 'hamburger',
            }
        }


class Recipe(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    image: Optional[str] = None
    imageType: Optional[str] = None
