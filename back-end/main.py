from fastapi import FastAPI
import funcao

#Como executar o fastapi
# python -m uvicorn main:app --reload


app = FastAPI(title="Gerenciador de produtos")

#Criando a rota inicial
@app.get("/")
def home():
    return {"mensagem": "Bem-vindo(a) Loja de Produtos!"}
