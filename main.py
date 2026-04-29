from src.interface import automacao_interface
from fastapi import FastAPI
from src.service import dados, dados_filtrados
import pandas as pd

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
        if not lista:
            return {"erro": "dados não carregados, use /livros/atualizar"}
        else:
            return lista
    except Exception as e:
        return {'Erro':str(e)}
    

#rota3
@app.get('/livros/{limit}')
def books(limit:int):
    try: 
        df = pd.DataFrame(lista)
        df = df[df['Price'] <= limit]
        df = df[['Title', 'Price']].sort_values(by='Price')
        df = df.to_dict('records')
        return df
    except Exception as e:
        return {'Erro':str(e)}
    

def main():
    automacao_interface()


if __name__ == "__main__":
    main()