from flask import Flask, jsonify, request
from flask_restful import Api
from sqlalchemy import exc

from models.time import Time
from util.dbutil import db
from models.jogador import Jogador
from models.pagamento import Pagamento
from models.pelada import Pelada
from models.user import User
from models.campo import Campo


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
        response.status_code = 201
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return


@app.route('/user/<int:id>', methods=['DELETE'])
def remove_usuario(id):
    usuario = User.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return "Removido com sucesso!"


# Metodos da Pelada


@app.route('/pelada/', methods=['GET'])
def get_peladas():
    peladas = Pelada.query.all()
    lista = []
    for item in peladas:
        lista.append(Pelada.to_json(item))
    return jsonify(lista)


@app.route('/pelada/', methods=['POST'])
def new_pelada():
    response = jsonify({})
    try:
        pelada = Pelada().from_json(request.json)
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
        pelada = Pelada.query.get_or_404(id)
        db.session.delete(pelada)
        db.session.commit()
        response.status_code=200
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


# Metodos do Jogador

@app.route('/jogador/', methods=['GET'])
def get_jogadores():
    jogadores = Jogador.query.all()
    lista = []
    for item in jogadores:
        lista.append(Jogador.to_json(item))
    return jsonify(lista)


@app.route('/jogador/', methods=['POST'])
def new_jogador():
    response = jsonify({})
    try:
        jogador = Jogador().from_json(request.json)
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
        jogador = Jogador.query.get_or_404(id)
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
        response.status_code = 202
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


#Metodos para campos


@app.route('/campo/', methods=['GET'])
def get_campos():
    campos = Campo.query.all()
    lista = []
    for item in campos:
        lista.append(Campo.to_json(item))
    return jsonify(lista)


@app.route('/campo/', methods=['POST'])
def new_campo():
    campo = Campo().from_json(request.json)
    response = jsonify({})
    try:
        db.session.add(campo)
        db.session.commit()
        response.status_code = 200
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


@app.route('/campo/<int:id>', methods=['DELETE'])
def remove_campo(id):
    response = jsonify({})
    try:
        campo = Campo.query.get_or_404(id)
        db.session.delete(campo)
        db.session.commit()
        response.status_code = 200
    except exc.SQLAlchemyError as e:
        response.status_code = 400
        print(e)
        db.session.remove()
        pass
    return response

# Metodo de boas vindas

@app.route("/")
def hello():
    db.create_all()

    return "Ola, Bem vindo ao Pelada FC"


if __name__ == "__main__":
    app.run(debug=True)

