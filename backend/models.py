from flask import Flask, jsonify
from config import app, db
from sqlalchemy import Column, Integer, String
from sqlalchemy import MEDIUMBLOB

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)

    def json(self):
        return jsonify({
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'senha': self.senha
        })
    
class Produto(db.Model):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    preco = Column(Integer, nullable=False)
    imagem = Column(MEDIUMBLOB, nullable=True)  # Armazena a imagem como BLOB

    def json(self):
        return jsonify({
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
        })