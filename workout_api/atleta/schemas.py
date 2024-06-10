from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=31)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=86.7)]
    altura: Annotated[str, Field(description='Altura do atleta', example=1.74)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M ou F', max_length=1)]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass