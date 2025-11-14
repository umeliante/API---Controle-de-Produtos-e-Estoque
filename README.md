📦 Sistema de Gerenciamento de Estoque

Aplicação de gerenciamento de estoque desenvolvida em Python, com interface web em Streamlit e integração com PostgreSQL para operações completas de CRUD (Create, Read, Update, Delete).
---

- 🚀 Tecnologias Utilizadas

Python 3.x

Streamlit – Interface web simples e interativa

PostgreSQL – Banco de dados relacional

pgAdmin4 – Gerenciamento do banco

psycopg2 / SQLAlchemy – Conexão com o banco (dependendo do que você usou)

---
- 📌 Funcionalidades

✔ Cadastro de produtos
✔ Consulta de itens do estoque
✔ Atualização de informações dos produtos
✔ Exclusão de itens
✔ Controle de quantidade em estoque
✔ Interface web intuitiva
✔ Conexão persistente com banco PostgreSQL
✔ Validação básica de dados

🔧 Instalação e Execução
1. Clone o repositório
git clone https://github.com/umeliante/API---Controle-de-Produtos-e-Estoque.git
cd estoque

2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Instale as dependências
pip install -r requirements.txt

4. Configure o banco PostgreSQL

Crie um banco (por exemplo, estoque_db) no pgAdmin4.

Execute no SQL:

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco NUMERIC(10,2),
    categoria VARCHAR(50)
);


Atualize as credenciais no arquivo database.py:

conn = psycopg2.connect(
    host="localhost",
    database="estoque_db",
    user="postgres",
    password="SUA_SENHA"
)

- ▶️ Rodando o projeto

    streamlit run app.py
---