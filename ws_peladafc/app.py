from flask import Flask, jsonify, request
from flask_restful import Api
from sqlalchemy import exc

from models.grupoUsuario import GrupoUsuario
from models.time import Time
from util.dbutil import db
from models.usuario import Usuario
from models.pagamento import Pagamento
from models.grupo import Grupo
from models.local import Local
from models.tipoUsuario import TipoUsuario
from models.redeSocial import RedeSocial


app = Flask(__name__)
api = Api(app)
app.debug = True


# Metodos do usuario

@app.route('/usuario/', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    lista = []
    for item in usuarios:
        lista.append(Usuario.to_json(item))
    return jsonify(lista)


@app.route('/usuario/<string:login>', methods=['GET'])
def get_usuario(login):
    user = Usuario.query.filter_by(username=login).first()
    return jsonify(user.to_json())


@app.route('/usuario/', methods=['POST'])
def new_usuario():
    response = jsonify({})
    try:
        usuario = Usuario().from_json(request.json)
        db.session.add(usuario)
        db.session.commit()
        response.status_code = 200
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        response.status_code = 400
        pass
    return response


@app.route('/usuario/<int:id>', methods=['DELETE'])
def remove_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return "Removido com sucesso!"


# Metodos da Grupo


@app.route('/grupo/', methods=['GET'])
def get_grupos():
    peladas = Grupo.query.all()
    lista = []
    for item in peladas:
        lista.append(Grupo.to_json(item))
    return jsonify(lista)


@app.route('/grupo/', methods=['POST'])
def new_grupo():
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


@app.route('/grupo/<int:id>', methods=['DELETE'])
def remove_grupo(id):
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


@app.route('/pagamento/<int:usuario_id>/<int:grupo_id>/<string:mes_ano>', methods=['DELETE'])
def remove_pagamento(usuario_id, grupo_id, mes_ano):
    response = jsonify({})
    try:
        resultado = Pagamento.query.filter_by(usuario_id=usuario_id, grupo_id=grupo_id, mes_ano=mes_ano).first()
        db.session.delete(resultado)
        db.session.commit()
        response.status_code = 200
    except exc.SQLAlchemyError as e:
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


@app.route('/time/', methods=['PUT'])
def update_time():
    time_alterado = Time().from_json(request.json)
    time = Time.query.get(time_alterado.id)
    time.from_json(request.json)
    response = jsonify({})
    try:
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


@app.route('/time/<int:id>', methods=['GET'])
def getbyid_time(id):
    response = jsonify({})
    try:
        time = Time.query.get_or_404(id)
        response.status_code = 200
    except exc.SQLAlchemyError as e:
        response.status_code = 400
        print(e)
        db.session.remove()
        pass
    return jsonify(time.to_json())


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

# Metodos do Grupo Usuario


@app.route('/grupousuario/', methods=['GET'])
def get_grupousuario():
    resultado = GrupoUsuario.query.all()
    lista = []
    for item in resultado:
        lista.append(GrupoUsuario.to_json(item))
    return jsonify(lista)


@app.route('/grupousuario/', methods=['POST'])
def new_grupousuario():
    response = jsonify({})
    try:
        print(request.json)
        resultado = GrupoUsuario().from_json(request.json)
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


@app.route('/grupousuario/<int:usuario_id>/<int:grupo_id>/<int:tipo_usuario_id>', methods=['DELETE'])
def remove_grupousuario(usuario_id, grupo_id, tipo_usuario_id):
    resultado = GrupoUsuario.query.filter_by(usuario_id=usuario_id, grupo_id=grupo_id, tipo_usuario_id=tipo_usuario_id).first()
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

