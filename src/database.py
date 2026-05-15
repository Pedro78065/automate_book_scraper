import mysql.connector
import pandas as pd

host = "localhost"
user = "root"
password = ""
database = "scraper"

def create_database(name_database):
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
        )
        cursor = conexao.cursor()

        comando = f"CREATE DATABASE IF NOT EXISTS {name_database} CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;"
        
        cursor.execute(comando)
        conexao.commit()
        print(f"database {name_database} criada com sucesso!")
    except mysql.connector.Error as e:
        print(f"Error:{e}")
    finally:
        if conexao.is_connected:
            cursor.close()
            conexao.close()


def  create_table(name_table):
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
        )
        cursor = conexao.cursor()

        comando = f"CREATE TABLE IF NOT EXISTS {name_table}(id int auto_increment not null, Title varchar(30) not null unique, Price float not null, primary key(id)) ENGINE = InnoDB CHARSET = utf8mb4;"

        cursor.execute(comando)
        conexao.commit()
        print(f"tabela {name_table} criada com sucesso!")
    except mysql.connector.Error as e:
        print(f"Erro:{e}") 
    finally:
        if conexao.is_connected:
            cursor.close()
            conexao.close()


def inserir_na_tabela(Title_inserir, Price_inserir):
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
        )
        cursor = conexao.cursor()
        
        comando = f"insert into dados (Title, Price) values (%s, %s);"

        cursor.execute(comando, (Title_inserir, Price_inserir))
        conexao.commit()
        print(f"o {Title_inserir} com o preço {Price_inserir} foi inserido com sucesso na tabela")
    except mysql.connector.Error as e:
        print(f"Erro:{e}")
    finally:
        if conexao.is_connected:
            cursor.close()
            conexao.close()


def deletar_database(name_database):
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
        )
        cursor = conexao.cursor()
        
        comando = f"drop database {name_database};"

        cursor.execute(comando)
        conexao.commit()
        print(f"a tabela {name_database} foi deletada com sucesso!")
        return {"database deletado com sucesso"}
    except mysql.connector.Error as e:
        print(f"Error:{e}")
    finally:
        if conexao.is_connected:
            cursor.close()
            conexao.close()


def visualizar_table(name_table):
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
        )
        cursor = conexao.cursor()

        comando = f"select Title,Price from {name_table}"

        cursor.execute(comando)
        ver = cursor.fetchall()
        print(ver)
        dados = pd.DataFrame(ver, columns = ["Title", "Price"])
        dados = dados.to_dict("records")
        return dados
    except mysql.connector.Error as e:
        print(f"Error:{e}")
    finally:
        if conexao.is_connected:
            cursor.close()
            conexao.close()


def visualizar_filter(name_table = "dados", valor_para_filtrar = 10000):
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
        )
        cursor = conexao.cursor()
        comando = f"select Price,Title from {name_table} where Price <= {valor_para_filtrar}"
        cursor.execute(comando)
        ver = cursor.fetchall()
        print(ver)
        dados = pd.DataFrame(ver, columns = ["Title", "Price"])
        dados = dados.to_dict("records")
        return dados
    except mysql.connector.Error as e:
        print(f"Error:{e}")
    finally:
        if conexao.is_connected:
            cursor.close()
            conexao.close()


