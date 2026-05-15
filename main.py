from src.interface import automacao_interface
from fastapi import FastAPI
from src.service import dados, dados_filtrados
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from src.database import visualizar_table, visualizar_filter, deletar_database
import uvicorn

lista = list()
lista_filtrada = list()

def atualizar(pages = 5):
    global lista
    df = dados(pages)
    lista = df


def atualizar_filter(limit = 10000):
    global lista_filtrada
    df = dados_filtrados(limit)
    lista_filtrada = df


#API
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://127.0.0.1:3000"],  # ou "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#rota
@app.get('/livros/atualizar')
def update(num_pages = 5):
    try:
        atualizar(num_pages)
        return {'dados':'atualizado!'}
    except Exception as e:
        return {'Error':str(e)}
    

#rota raiz
@app.get('/')
def server():
    try:
        return {'servidor': 'está no ar!'}
    except Exception as e:
        return {'Error':str(e)}


#rota2
@app.get('/livros')
def livros():
    try:
        return visualizar_table("dados")
    except Exception as e:
        return {"Erro":str(e)}

    
@app.get('/deletar')
def deletar():
    try:
        deletar_database("scraper")
        return {"sucesso ao deletar dados"}
    except Exception as e:
        return{'Erro':str(e)}
    
   
#rota3
@app.get('/livros/{limit}')
def books(limit:int):
    try: 
        return visualizar_filter("dados",f"{limit}")
    except Exception as e:
        return {'Erro':str(e)}
    
      
def main():
    automacao_interface()


if __name__ == "__main__":
    main()
    uvicorn.run(
        app="main:app",
        host="localhost",
        port=8000,
        reload=True
    )