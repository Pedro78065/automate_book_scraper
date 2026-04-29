import tkinter as tk
import threading
from src.auto_scraper import scraper
from src.service import dados, dados_filtrados, salvar_todos_csv

def automacao_interface():

    def rodar_scraper():
        try:
            numeric_pages = int(input('Digite o número de páginas: '))
            limit = int(input('Digite o valor máximo do livros: '))
        except Exception as e:
            print(f'Erro:{e}')   
        try:
            salvar_todos_csv(numeric_pages, limit)
            texto.config(text='Automação concluída!')
        except Exception as e:
            print(f'Error:{e}')


    def botao():
        texto.config(text='Automatizando...')
        thread = threading.Thread(target=rodar_scraper)
        thread.start()


    janela = tk.Tk()
    janela.title('AUTOMAÇÃO_LIVROS')
    janela.geometry('400x300')

    texto = tk.Label(janela, text='Clique no botão para automatizar o scraping')
    texto.pack()

    automatizar = tk.Button(janela, text='Press', command=botao)
    automatizar.pack()

    janela.mainloop()