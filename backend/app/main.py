from fastapi import FastAPI, status, HTTPException
from app.schemas import LivroCriar, LivroResposta, Genero
from datetime import datetime, timezone

import random

app = FastAPI(title = "Estante API")


# =================================

livros_list = [{"id" : 1 , "titulo" : "A empregada", "autor" : "Frida", "genero" : "suspense" , "meta_semanal" : 3, "encerrado" : False, "criado_em" : "2026-10-06T04:31:14.654Z" , "data_termino" : None},
               {"id" : 2 , "titulo" : "Suicidas", "autor" : "Raphaek Montes", "genero" : "suspense" , "meta_semanal" : 4 , "encerrado" : False, "criado_em" : "2026-10-06T04:31:14.654Z" , "data_termino" : None},
               {"id" : 3 , "titulo" : "aprendendo algoritimos", "autor" : "Fabricio Braz", "genero" : "outro" , "meta_semanal" : 5, "encerrado" : False, "criado_em" : "2026-10-06T04:31:14.654Z" , "data_termino" : None}]

# =================================


@app.get("/health")
def health():
    return {"status" : 200 , "version" : "0.1.0"}

    

@app.get("/livros", response_model= list[LivroResposta], status_code= status.HTTP_200_OK)
def listar_livros(genero : Genero | None = None, limite : int = 2):

    count = 0
    resposta = []

    for livro in livros_list:

        if (count < limite ):

            if genero :

                if genero == livro["genero"]:
                    resposta.append(livro)
                    count += 1

            else:

                resposta.append(livro)
                count += 1

        else :

            return resposta


    return resposta




@app.post("/livros", status_code= status.HTTP_201_CREATED, response_model= LivroResposta)
def criar_livro(dados : LivroCriar):

    livro = dados.model_dump()

    livro["id"] = random.randint(0 , 100)

    livro["encerrado"] = False

    livro["criado_em"] = datetime.now(timezone.utc)

    livros_list.append(livro)

    return livro
 



@app.get("/livros/{livro_id}", status_code= status.HTTP_200_OK ,response_model=LivroResposta)
def localizar_livro(id : int):

    for livro in livros_list:

        if livro["id"] == id:

            return livro


    raise HTTPException(status_code=404, detail="livro não encontrado")