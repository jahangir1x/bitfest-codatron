from typing import Optional

from pydantic import ConfigDict, BaseModel


# Shared properties
class SuggestionBase(BaseModel):
    details: Optional[str] = None


# Properties to receive on Suggestion creation
class SuggestionCreate(SuggestionBase):
    details: str


# Properties to receive on Suggestion update
class SuggestionUpdate(SuggestionBase):
    pass


# Properties shared by models stored in DB
class SuggestionInDBBase(SuggestionBase):
    id: int
    details: str
    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class SuggestionResponse(BaseModel):
    details: str


# Properties properties stored in DB
class SuggestionInDB(SuggestionInDBBase):
    pass
