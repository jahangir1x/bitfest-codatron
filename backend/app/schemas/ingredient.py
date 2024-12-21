from typing import Optional

from pydantic import ConfigDict, BaseModel


# Shared properties
class IngredientBase(BaseModel):
    name: Optional[str] = None


# Properties to receive on Ingredient creation
class IngredientCreate(IngredientBase):
    name: str


# Properties to receive on Ingredient update
class IngredientUpdate(IngredientBase):
    pass


# Properties shared by models stored in DB
class IngredientInDBBase(IngredientBase):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Ingredient(IngredientInDBBase):
    pass


# Properties properties stored in DB
class IngredientInDB(IngredientInDBBase):
    pass
