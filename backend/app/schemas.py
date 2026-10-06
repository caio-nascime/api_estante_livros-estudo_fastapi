from fastapi import FastAPI, status
from pydantic import Field, BaseModel, field_validator, ConfigDict
from enum import Enum
from datetime import date, datetime, timezone



class Genero(str, Enum):

    suspense = "suspense"
    drama = "drama"
    acao = "acao"
    romance = "romance"
    outro = "outro"




class LivroCriar(BaseModel):

    model_config = ConfigDict(extra="forbid")

    titulo : str = Field( min_length = 1 , max_length = 200)
    autor : str | None = None
    genero : Genero = Genero.outro
    meta_semanal : int = Field( ge = 1 , le = 7)
    data_termino : date | None = None


    @field_validator("titulo")
    @classmethod
    def normalizar_titulo(cls, titulo : str | None):

        if titulo is None:

            raise ValueError("O título é obrigatório")
            return None

        else :

            titulo = " ".join(titulo.split())
            if not titulo :
                raise ValueError("O título deve ser preenchido")

            return titulo


    @field_validator("data_termino")
    @classmethod
    def verificar_data_termino(cls, data_termino : date | None):

        if data_termino is not None and data_termino < datetime.now(timezone.utc).date():

            raise ValueError("data_termino não pode ser anterior à data de criação")

        else :
            
            return data_termino 







class LivroResposta(BaseModel):

    titulo : str = Field( min_length = 1 , max_length = 200)
    autor : str | None = None
    genero : Genero = Genero.outro
    meta_semanal : int = Field( ge = 1 , le = 7)
    data_termino : date | None = None
    id : int
    encerrado : bool = False
    criado_em : datetime
    
