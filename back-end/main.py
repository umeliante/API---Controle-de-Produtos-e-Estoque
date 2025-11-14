from fastapi import FastAPI
import funcao

#Como executar o fastapi
# python -m uvicorn main:app --reload


app = FastAPI(title="Gerenciador de produtos")

#Criando a rota inicial
@app.get("/")
def home():
    return {"mensagem": "Bem-vindo(a) Loja de Produtos!"}

@app.post("/produtos")
def cadastrar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.cadastrar_produto(nome, categoria, preco, quantidade)
    return{"200": "produto cadastrado com sucesso!"}

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    lista = []
    for linha in produtos:
        lista.append(
            {
                "id": linha[0],
                "nome": linha[1],
                "categoria": linha[2],
                "preco": linha[3],
                "quantidade": linha[4]
            }
        )
    return{"produtos": lista}

@app.delete("/produtos/{id_produtos}")
def deletar_produtos(id_produtos: int):
    produtos = funcao.buscar_produtos(id_produtos)
    if produtos:
        funcao.deletar_produtos(id_produtos)
        return {"mensagem": "produto excluído com sucesso!"}
    else:
        return {"erro:": "produto não encontrado"}

@app.atualizar("/produtos/{id_produtos}")
def atulizar_produtos(id_produtos: int):
    produtos = funcao.atualizar_produto(id_produtos)
    if produtos:
        funcao.atualizar_produto(id_produtos)
        return {"mensagem": "Produto atualizado com sucesso!"}
    else:
        return {"erro:": "Produto não encontrado"}

