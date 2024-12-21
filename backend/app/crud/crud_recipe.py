from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate, RecipeUpdate, RecipeResponse


class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    def process_recipe(self, obj_in: RecipeCreate) -> RecipeResponse:
        parsed = jsonable_encoder(obj_in)
        print("obj_in: ", parsed)
        return RecipeResponse(status="success")


recipe = CRUDRecipe(RecipeCreate)
