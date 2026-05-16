# 📚 Automate Book Scraper-(feito por:"Pedro.H.C")

Automação para coleta de dados de livros de forma simples e rápida, com exportação em CSV e disponibilização dos dados via API com FastAPI.


---

## Funcionalidades

* Te economiza horas de trabalho manual
* Scraping automático de livros
* Extração de título, preço e outras informações
* Exportação para CSV
* cria api localhost que mostra dados e scraping dos livros
- API local para consulta e filtragem dos dados

---

## ⚙️ Requisitos

Antes de começar, você precisa ter instalado:

* Python 3.10+
* pip

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/Pedro78065/automate_book_scraper.git
cd automate_book_scraper
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Instale os navegadores do Playwright:

```bash
playwright install
```
---
## WEB COMO USAR

execute main.py e abra o arquivo index.html no navegador.

---

## Como usar

Execute o script principal:

```bash
python main.py
```
---

## Como criar api

no terminal do projeto(book_scraper) digite:

```bash
uvicorn main:app --reload
```
---
## Endpoints da API
* /livros/atualizar (sempre que iniciar a api, use para o scraper coletar dados pelo primeira vez)
* /livros
* /livros/20 (ou preço que deseja filtrar)

---

## ⚠️ Problemas comuns

### ❌ Erro: "playwright not found"

Solução:

```bash
pip install playwright
```

---

### ❌ Erro: navegador não abre

Solução:

```bash
playwright install
```

---

### ❌ Interface não abre (Tkinter)

* Certifique-se de estar rodando no PC
* Não funciona corretamente em Termux/Android

---

## 📄 Licença

Este projeto é apenas para fins educacionais
