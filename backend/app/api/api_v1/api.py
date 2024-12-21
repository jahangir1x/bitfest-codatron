from fastapi import APIRouter

from app.api.api_v1.endpoints import ingredients

api_router = APIRouter()
api_router.include_router(ingredients.router, prefix="/ingredients", tags=["ingredients"])
