from flask import Flask
from config import app, db

# importação das tabelas do banco de dados
from models import *

# importação das funções de CRUD e rotas para arquivos html
from crud import *
from rotas_html import *

if __name__ == '__main__':
    db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)