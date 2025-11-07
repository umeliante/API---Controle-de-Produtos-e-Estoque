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
cadastrar_produto(nome="chinelo", categoria="kenner", preco=100, quantidade=2)

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

