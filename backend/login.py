from config import app, db
from flask import render_template, request, jsonify, session
from models import Usuario
from werkzeug.security import check_password_hash


def login_usuario(f):
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            return jsonify({'aviso': 'Usuário não autenticado'}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        
        usuario = Usuario.find_one({'nome': nome})
        if usuario and check_password_hash(usuario.senha, senha):
            session['usuario_id'] = usuario.id
            return jsonify({'aviso': 'Login feito com sucesso'}), 200
        else:
            return jsonify({'aviso': 'Login ou senha inválidos'}), 401
    
    return render_template('login.html')

@app.route('/logout')
@login_usuario
def logout():
    if 'usuario_id' in session:
        session.pop('usuario_id', None)
        return jsonify({'aviso': 'Logout feito com sucesso'}), 200
    else:
        return jsonify({'aviso': 'Erro interno ao fazer logout'}), 500
