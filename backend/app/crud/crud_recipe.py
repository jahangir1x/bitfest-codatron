from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate, RecipeUpdate


class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    def process_recipe(self, db: Session, obj_in: RecipeCreate) -> Recipe:
        parsed = jsonable_encoder(obj_in)
        print("obj_in: ", parsed)
        db_obj = Recipe(details=parsed["details"])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


recipe = CRUDRecipe(RecipeCreate)
