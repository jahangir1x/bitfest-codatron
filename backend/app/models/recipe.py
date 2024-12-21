from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .recipe import Recipe  # noqa: F401


class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True)
    details = Column(String, index=False)
