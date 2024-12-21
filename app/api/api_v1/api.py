from fastapi import APIRouter

from app.api.api_v1.endpoints import ingredients, recipes, suggestions

api_router = APIRouter()
api_router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(
    ingredients.router, prefix="/ingredients", tags=["ingredients"]
)
api_router.include_router(
    suggestions.router, prefix="/suggestions", tags=["suggestions"]
)
