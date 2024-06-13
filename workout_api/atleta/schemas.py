from typing import Annotated, Optional
from pydantic import BaseModel, Field, PositiveFloat
from workout_api.c_t.schemas import CentroTreinamentoAtleta
from workout_api.categorias.schemas import CategoriaIn
from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=31)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=86.7)]
    altura: Annotated[str, Field(description='Altura do atleta', example=1.74)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M ou F', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(description='Idade do atleta', example=31)]