# 📚 Automate Book Scraper 
### (feito por:"Pedro.H.C")

Automação para coleta de dados de livros de forma simples e rápida.

---

## Funcionalidades

* Scraping automático de livros
* Extração de título, preço e outras informações
* Exportação para CSV

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

## Como usar

Execute o script principal:

```bash
python main.py
```

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

## Observações importantes

* O uso de scraping pode ser limitado por alguns sites
* Evite fazer muitas requisições em pouco tempo (pode causar bloqueio)

---

## 📄 Licença

Este projeto é apenas para fins educacionais
