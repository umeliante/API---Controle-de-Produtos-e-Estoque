from conexao import conector

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER
            )            
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()

def cadastrar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s,%s)",
                (nome, categoria, preco, quantidade)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastrar produtos {erro}") 
        finally:
            cursor.close()
            conexao.commit()

def listar_produtos():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos"
                )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar produtos {erro}")
            return [] 
        finally:
            cursor.close()
            conexao.commit()

def atualizar_produto(id_produtos, nova_quantidade):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET quantidade = %s WHERE id = %s", (nova_quantidade, id_produtos)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar o produto {erro}")
   
        finally:
            cursor.close()
            conexao.commit()

def deletar_produto(id_produtos):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s", (id_produtos,)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar o produto {erro}")
   
        finally:
            cursor.close()
            conexao.commit()

def buscar_produtos(id_produtos):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos WHERE id = %s", (id_produtos,)
                )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar o produto {erro}")
            return []
        finally:
            cursor.close()
            conexao.commit()

