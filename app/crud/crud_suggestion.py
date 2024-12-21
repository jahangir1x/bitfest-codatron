from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.ingredient import Ingredient
from app.models.suggestion import Suggestion
from app.schemas.suggestion import (
    SuggestionCreate,
    SuggestionResponse,
    SuggestionUpdate,
)


class CRUDSuggestion(CRUDBase[Suggestion, SuggestionCreate, SuggestionUpdate]):
    def process_suggestion(
        self, db: Session, obj_in: SuggestionCreate
    ) -> SuggestionResponse:
        details = jsonable_encoder(obj_in)
        all_ingredients = db.query(Ingredient).all()
        print("obj_in: ", details)
        print("all_ingredients: ", all_ingredients)
        return SuggestionResponse(details="success")


suggestion = CRUDSuggestion(Suggestion)
