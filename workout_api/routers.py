from fastapi import APIRouter
from workout_api.atleta.controller import router as atleta
from workout_api.categorias.controller import router as categorias
from workout_api.c_t.controller import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['Atletas'])
api_router.include_router(categorias, prefix='/categorias', tags=['Categorias'])
api_router.include_router(centro_treinamento, prefix='/centros_treinamento', tags=['Centros_Treinamento'])
