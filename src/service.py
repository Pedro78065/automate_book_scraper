import pandas as pd
from src.auto_scraper import scraper

def dados(max_pages = 5):
    df = scraper(max_pages)
    df.to_csv('produtos.csv', index=False)
    df = pd.read_csv('produtos.csv', sep=',')
    df["Price"] = df["Price"].str.extract(r"£(\d+\.\d+)").astype(float)
    df = df.to_dict(orient='records')
    return df


def dados_filtrados(limite = 10000):
    df = dados()
    df = pd.DataFrame(df)
    livro_barato = df[df['Price'] <= limite]
    livro_barato = livro_barato[['Title', 'Price']].sort_values(by='Price')
    livro_barato.to_csv('LIVROS_FILTRADOS.csv', index=False)
    livro_barato = livro_barato.to_dict(orient='records')
    return livro_barato

def salvar_todos_csv(max_pages = 5, limite = 10000):
    df = scraper(max_pages)
    df.to_csv('produtos.csv', index=False)
    df = pd.read_csv('produtos.csv', sep=',')
    df["Price"] = df["Price"].str.extract(r"£(\d+\.\d+)").astype(float)
    livros_filtrados = df[df["Price"] <= limite]
    livros_filtrados = livros_filtrados[['Title', 'Price']].sort_values(by='Price')
    livros_filtrados.to_csv('LIVROS_FILTRADOS.csv')