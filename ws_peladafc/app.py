from flask import Flask, jsonify, request
from flask_restful import Api
from sqlalchemy import exc

from models.time import Time
from util.dbutil import db
from models.usuario import Usuario
from models.pagamento import Pagamento
from models.grupo import Grupo
from models.user import User
from models.local import Local
from models.tipoUsuario import TipoUsuario
from models.redeSocial import RedeSocial


app = Flask(__name__)
api = Api(app)
app.debug = True

# if not app.debug:
#     import logging
#     from logging.handlers import RotatingFileHandler
#     file_handler = RotatingFileHandler('python.log', maxBytes=1024 * 1024 * 100, backupCount=20)
#     file_handler.setLevel(logging.ERROR)
#     formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#     file_handler.setFormatter(formatter)
#     app.logger.addHandler(file_handler)


# Metodos do usuario

@app.route('/user/', methods=['GET'])
def get_usuarios():
    usuarios = User.query.all()
    lista = []
    for item in usuarios:
        lista.append(User.to_json(item))
    return jsonify(lista)


@app.route('/user/<string:login>', methods=['GET'])
def get_usuario(login):
    user = User.query.filter_by(username=login).first()
    return jsonify(user.to_json())


@app.route('/user/', methods=['POST'])
def new_usuario():
    response = jsonify({})
    try:
        usuario = User().from_json(request.json)
        db.session.add(usuario)
        db.session.commit()
        response.status_code = 200
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


@app.route('/user/<int:id>', methods=['DELETE'])
def remove_usuario(id):
    usuario = User.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return "Removido com sucesso!"


# Metodos da Grupo


@app.route('/pelada/', methods=['GET'])
def get_peladas():
    peladas = Grupo.query.all()
    lista = []
    for item in peladas:
        lista.append(Grupo.to_json(item))
    return jsonify(lista)


@app.route('/pelada/', methods=['POST'])
def new_pelada():
    response = jsonify({})
    try:
        pelada = Grupo().from_json(request.json)
        db.session.add(pelada)
        db.session.commit()
        response.status_code = 200
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


@app.route('/pelada/<int:id>', methods=['DELETE'])
def remove_pelada(id):
    response = jsonify({})
    try:
        pelada = Grupo.query.get_or_404(id)
        db.session.delete(pelada)
        db.session.commit()
        response.status_code=200
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


# Metodos do Usuario

@app.route('/jogador/', methods=['GET'])
def get_jogadores():
    jogadores = Usuario.query.all()
    lista = []
    for item in jogadores:
        lista.append(Usuario.to_json(item))
    return jsonify(lista)


@app.route('/jogador/', methods=['POST'])
def new_jogador():
    response = jsonify({})
    try:
        jogador = Usuario().from_json(request.json)
        db.session.add(jogador)
        db.session.commit()
        response.status_code = 200
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


@app.route('/jogador/<int:id>', methods=['DELETE'])
def remove_jogador(id):
    response = jsonify({})
    try:
        jogador = Usuario.query.get_or_404(id)
        db.session.delete(jogador)
        db.session.commit()
        response.status_code = 200
    except exc.SQLAlchemyError as e:
        response.status_code = 400
        print(e)
        db.session.remove()
        pass
    return response

# Metodos do Pagamento


@app.route('/pagamento/', methods=['GET'])
def get_pagamentos():
    pagamentos = Pagamento.query.all()
    lista = []
    for item in pagamentos:
        lista.append(Pagamento.to_json(item))
    return jsonify(lista)


@app.route('/pagamento/', methods=['POST'])
def new_pagamento():
    pagamento = Pagamento().from_json(request.json)
    response = jsonify({})
    try:
        db.session.add(pagamento)
        db.session.commit()
        response.status_code = 200
    except exc.IntegrityError as e:
        print(e)
        response.status_code = 400
        db.session.remove()
        pass
    return response

# Metodos para times


@app.route('/time/', methods=['GET'])
def get_times():
    times = Time.query.all()
    lista = []
    for item in times:
        lista.append(Time.to_json(item))
    return jsonify(lista)


@app.route('/time/', methods=['POST'])
def new_time():
    time = Time().from_json(request.json)
    response = jsonify({})
    try:
        db.session.add(time)
        db.session.commit()
        response.status_code = 200
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


@app.route('/time/<int:id>', methods=['DELETE'])
def remove_time(id):
    response = jsonify({})
    try:
        time = Time.query.get_or_404(id)
        db.session.delete(time)
        db.session.commit()
        response.status_code = 200
    except exc.SQLAlchemyError as e:
        response.status_code = 400
        print(e)
        db.session.remove()
        pass
    return response


#Metodos para local


@app.route('/local/', methods=['GET'])
def get_locals():
    locals = Local.query.all()
    lista = []
    for item in locals:
        lista.append(Local.to_json(item))
    return jsonify(lista)


@app.route('/local/', methods=['POST'])
def new_local():
    local = Local().from_json(request.json)
    response = jsonify({})
    try:
        db.session.add(local)
        db.session.commit()
        response.status_code = 200
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


@app.route('/local/<int:id>', methods=['DELETE'])
def remove_local(id):
    response = jsonify({})
    try:
        local = Local.query.get_or_404(id)
        db.session.delete(local)
        db.session.commit()
        response.status_code = 200
    except exc.SQLAlchemyError as e:
        response.status_code = 400
        print(e)
        db.session.remove()
        pass
    return response


# Metodos do tipo usuario


@app.route('/tipousuario/', methods=['GET'])
def get_tipousuarios():
    tipousuarios = TipoUsuario.query.all()
    lista = []
    for item in tipousuarios:
        lista.append(TipoUsuario.to_json(item))
    return jsonify(lista)


@app.route('/tipousuario/', methods=['POST'])
def new_tipousuario():
    response = jsonify({})
    try:
        tipousuario = TipoUsuario().from_json(request.json)
        db.session.add(tipousuario)
        db.session.commit()
        response.status_code = 200
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


@app.route('/tipousuario/<int:id>', methods=['DELETE'])
def remove_tipousuario(id):
    print(id)
    tipousuario = TipoUsuario.query.get_or_404(id)
    db.session.delete(tipousuario)
    db.session.commit()
    return "Removido com sucesso!"

# Metodos do Rede Social


@app.route('/redesocial/', methods=['GET'])
def get_redesocial():
    resultado = RedeSocial.query.all()
    lista = []
    for item in resultado:
        lista.append(RedeSocial.to_json(item))
    return jsonify(lista)


@app.route('/redesocial/', methods=['POST'])
def new_redesocial():
    response = jsonify({})
    try:
        print(request.json)
        resultado = RedeSocial().from_json(request.json)
        print(resultado)
        db.session.add(resultado)
        db.session.commit()
        response.status_code = 200
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


@app.route('/redesocial/<int:id>', methods=['DELETE'])
def remove_redesocial(id):
    resultado = RedeSocial.query.get_or_404(id)
    db.session.delete(resultado)
    db.session.commit()
    return "Removido com sucesso!"

# Metodo de boas vindas

@app.route("/")
def hello():
    return "Ola, Bem vindo ao Grupo FC"

@app.route("/createdb")
def createdb():
    db.create_all()
    return "Ola, seu banco foi criado !"

@app.route("/dropdb")
def dropdb():
    db.drop_all()
    return "Ola, seu banco foi apagado !"


if __name__ == "__main__":
    app.run(debug=True)

