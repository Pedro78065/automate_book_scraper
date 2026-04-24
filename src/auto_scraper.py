from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
import pandas as pd

def scraper(num_page = 5, limite = 90):
    """
    num_page: serve para definir quantas páginas vc quer coletar os dados.
    """
    try:
        num_page = int(input('Digite o número de páginas: '))
        limite = int(input('Digite o valor máximo do livros: '))
    except Exception as e:
        print(f'Erro:{e}')

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            Stealth().apply_stealth_sync(page)

            page.goto('https://books.toscrape.com/')
            page.wait_for_load_state('load')
            page.wait_for_timeout(3000)
            numeric_pages = 1
            list_produtos = []

            try:
                while numeric_pages <= num_page:
                    products = page.query_selector_all('li.col-xs-6.col-sm-4.col-md-3.col-lg-3')
                    for product in products:
                        title_element =  product.query_selector('h3')
                        price_element = product.query_selector('.product_price')

                        title = title_element.inner_text() if title_element else 'NULL'
                        price =  price_element.inner_text() if price_element else 'NULL'
                        list_produtos.append({
                            'Title':title,
                            'Price':price
                        })
            
                    print(f'página = {numeric_pages}')
                    numeric_pages +=1
                    page.wait_for_timeout(3000)
                    next_button = page.get_by_role('link', name = 'next')
                    if next_button:
                        next_button.click()
                    else:
                        break
            except Exception as e:
                print(f'Erro:{e}')

            df = pd.DataFrame(list_produtos)
            df.to_csv('produtos.csv', index=False)
            df = pd.read_csv('produtos.csv', sep=',')
            print(f'produtos cadastrados: {len(list_produtos)}')
            df["Price"] = df["Price"].str.extract(r"£(\d+\.\d+)").astype(float)
            livro_barato = df[df['Price'] <= limite]
            livro_barato.to_csv('LIVROS_FILTRADOS.csv', index=False)

        except Exception as e:
            print(f'Erro:{e}')

        finally:
            context.close()
            browser.close()
            