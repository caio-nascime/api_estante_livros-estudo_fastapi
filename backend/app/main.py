from fastapi import FastAPI

app = FastAPI(title = "Estante API")


# =================================

livros_list = [{"id" : 1 , "titulo" : "a empregada", "autor" : "Frida", "genero" : "suspense" , "meta_semanal" : 3},
               {"id" : 2 , "titulo" : "Suicidas", "autor" : "Raphaek Montes", "genero" : "suspense" , "meta_semanal" : 4},
               {"id" : 3 , "titulo" : "aprendendo algoritimos", "autor" : "Fabricio Braz", "genero" : "educacao" , "meta_semanal" : 5}]

# =================================


@app.get("/health")
def health():
    return {"status" : 200 , "version" : "0.1.0"}

    

@app.get("/livros")
def listar_livros(genero : str | None = None, limite : int = 2):

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

            return {"status" : 200 , "livros" : resposta}


    return {"status" : 200 , "livros" : resposta}




@app.get("/livros/{livro_id}")
def localizar_livro(id : int):

    for livro in livros_list:

        if livro["id"] == id:

            return {"status" : 200 , "resposta" : livro}


    return {"status" : 404 , "resposta" : "livro não encontrado"}