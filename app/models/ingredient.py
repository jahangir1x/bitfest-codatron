from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .ingredient import Ingredient  # noqa: F401


class Ingredient(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=False)
