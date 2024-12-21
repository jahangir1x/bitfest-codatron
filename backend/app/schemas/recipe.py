from typing import Optional

from pydantic import ConfigDict, BaseModel


# Shared properties
class RecipeBase(BaseModel):
    details: Optional[str] = None


# Properties to receive on Recipe creation
class RecipeCreate(RecipeBase):
    details: str


# Properties to receive on Recipe update
class RecipeUpdate(RecipeBase):
    pass


# Properties shared by models stored in DB
class RecipeInDBBase(RecipeBase):
    id: int
    details: str
    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Recipe(RecipeInDBBase):
    pass


# Properties properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass
