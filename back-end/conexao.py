import psycopg2
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

def conector():
    try:
        conexao = psycopg2.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conexao.cursor()
        print("Conexão com PostgreSQL bem-sucedida!")
        return conexao, cursor

    except Exception as erro:
        print(f"Erro de conexão: {erro}")
        return None, None
conector()