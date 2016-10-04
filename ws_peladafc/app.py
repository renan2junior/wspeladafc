from flask import Flask, jsonify, request, make_response
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
    try:
        usuarios = Usuario.query.all()
        lista = []
        for item in usuarios:
            lista.append(Usuario.to_json(item))
        return make_response(jsonify(lista), 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/usuario/<string:login>', methods=['GET'])
def get_usuario(login):
    try:
        usuario = Usuario.query.filter_by(email=login).first()
        if(usuario):
            rs_usuario = jsonify(usuario.to_json())
        else:
            rs_usuario = jsonify({})
        return make_response(rs_usuario, 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/usuario/<int:id>', methods=['GET'])
def get_usuariobyid(id):
    try:
        usuario = Usuario.query.get_or_404(id)
        if (usuario):
            rs_usuario = jsonify(usuario.to_json())
        else:
            rs_usuario = jsonify({})
        return make_response(rs_usuario, 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/usuario/', methods=['POST'])
def new_usuario():
    try:
        usuario = Usuario().from_json(request.json)
        db.session.add(usuario)
        db.session.commit()
        if (usuario):
            rs_usuario = jsonify(usuario.to_json())
        else:
            rs_usuario = jsonify({})
        return make_response(rs_usuario, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/usuario/', methods=['PUT'])
def update_usuario():
    usuario_alterado = Usuario().from_json(request.json)
    usuario = Usuario.query.get(usuario_alterado.id)
    usuario.from_json(request.json)
    try:
        db.session.commit()
        return make_response(usuario, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/usuario/<int:id>', methods=['DELETE'])
def remove_usuario(id):
    try:
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return make_response("Removido com sucesso!", 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


# Metodos da Grupo


@app.route('/grupo/', methods=['GET'])
def get_grupos():
    try:
        grupos = Grupo.query.all()
        lista = []
        for item in grupos:
            lista.append(Grupo.to_json(item))
        return make_response(jsonify(lista), 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/grupo/<int:id>', methods=['GET'])
def get_grupobyid(id):
    try:
        grupo = Grupo.query.get_or_404(id)
        if (grupo):
            rs_grupo = jsonify(grupo.to_json())
        else:
            rs_grupo = jsonify({})
        return make_response(rs_grupo, 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/grupo/', methods=['POST'])
def new_grupo():
    try:
        grupo = Grupo().from_json(request.json)
        db.session.add(grupo)
        db.session.commit()
        if (grupo):
            rs_grupo = jsonify(grupo.to_json())
        else:
            rs_grupo = jsonify({})
        return make_response(rs_grupo, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/grupo/', methods=['PUT'])
def update_grupo():
    grupo_alterado = Grupo().from_json(request.json)
    grupo = Time.query.get(grupo_alterado.id)
    grupo.from_json(request.json)
    try:
        db.session.commit()
        return make_response(grupo, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/grupo/<int:id>', methods=['DELETE'])
def remove_grupo(id):
    try:
        grupo = Grupo.query.get_or_404(id)
        db.session.delete(grupo)
        db.session.commit()
        return make_response("Removido com sucesso!", 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


# Metodos do Pagamento


@app.route('/pagamento/', methods=['GET'])
def get_pagamentos():
    try:
        pagamentos = Pagamento.query.all()
        lista = []
        for item in pagamentos:
            lista.append(Pagamento.to_json(item))
        return make_response(jsonify(lista), 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/pagamento/', methods=['POST'])
def new_pagamento():
    try:
        pagamento = Pagamento().from_json(request.json)
        db.session.add(pagamento)
        db.session.commit()
        if (pagamento):
            rs_pagamento = jsonify(pagamento.to_json())
        else:
            rs_pagamento = jsonify({})
        return make_response(rs_pagamento, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/pagamento/<int:usuario_id>/<int:grupo_id>/<string:mes_ano>', methods=['DELETE'])
def remove_pagamento(usuario_id, grupo_id, mes_ano):
    try:
        resultado = Pagamento.query.filter_by(usuario_id=usuario_id, grupo_id=grupo_id, mes_ano=mes_ano).first()
        db.session.delete(resultado)
        db.session.commit()
        return make_response("Removido com sucesso!", 200)
    except exc.SQLAlchemyError as e:
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


# Metodos para times


@app.route('/time/', methods=['GET'])
def get_times():
    try:
        times = Time.query.all()
        lista = []
        for item in times:
            lista.append(Time.to_json(item))
        return make_response(jsonify(lista), 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/time/', methods=['POST'])
def new_time():
    try:
        time = Time().from_json(request.json)
        db.session.add(time)
        db.session.commit()
        if (time):
            rs_time = jsonify(time.to_json())
        else:
            rs_time = jsonify({})
        return make_response(rs_time, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/time/', methods=['PUT'])
def update_time():
    time_alterado = Time().from_json(request.json)
    time = Time.query.get(time_alterado.id)
    time.from_json(request.json)
    try:
        db.session.commit()
        return make_response(time, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/time/<int:id>', methods=['DELETE'])
def remove_time(id):
    response = jsonify({})
    try:
        time = Time.query.get_or_404(id)
        db.session.delete(time)
        db.session.commit()
        return make_response("Removido com sucesso!", 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/time/<int:id>', methods=['GET'])
def getbyid_time(id):
    try:
        time = Time.query.get_or_404(id)
        if (time):
            rs_time = jsonify(time.to_json())
        else:
            rs_time = jsonify({})
        return make_response(rs_time, 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


#Metodos para local


@app.route('/local/', methods=['GET'])
def get_locals():
    try:
        loacais = Local.query.all()
        lista = []
        for item in loacais:
            lista.append(Local.to_json(item))
        return make_response(jsonify(lista), 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/local/<int:id>', methods=['GET'])
def get_localbyid(id):
    try:
        local = Local.query.get_or_404(id)
        if (local):
            rs_local = jsonify(local.to_json())
        else:
            rs_local = jsonify({})
        return make_response(rs_local, 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/local/', methods=['POST'])
def new_local():
    local = Local().from_json(request.json)
    try:
        db.session.add(local)
        db.session.commit()
        return make_response(jsonify(local.to_json()), 200)
    except exc.IntegrityError as e:
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/local/', methods=['PUT'])
def update_local():
    local_alterado = Local().from_json(request.json)
    local = Local.query.get(local_alterado.id)
    local.from_json(request.json)
    try:
        db.session.commit()
        return make_response(local, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/local/<int:id>', methods=['DELETE'])
def remove_local(id):
    try:
        local = Local.query.get_or_404(id)
        db.session.delete(local)
        db.session.commit()
        return make_response("Removido com sucesso!", 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


# Metodos do tipo usuario


@app.route('/tipousuario/', methods=['GET'])
def get_tipousuarios():
    try:
        tipousuarios = TipoUsuario.query.all()
        lista = []
        for item in tipousuarios:
            lista.append(TipoUsuario.to_json(item))
        return make_response(jsonify(lista), 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/tipousuario/', methods=['POST'])
def new_tipousuario():
    try:
        tipousuario = TipoUsuario().from_json(request.json)
        db.session.add(tipousuario)
        db.session.commit()
        if (tipousuario):
            rs = jsonify(tipousuario.to_json())
        else:
            rs = jsonify({})
        return make_response(rs, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/tipousuario/<int:id>', methods=['DELETE'])
def remove_tipousuario(id):
    try:
        tipousuario = TipoUsuario.query.get_or_404(id)
        db.session.delete(tipousuario)
        db.session.commit()
        return make_response("Removido com sucesso!", 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)

# Metodos do Rede Social


@app.route('/redesocial/', methods=['GET'])
def get_redesocial():
    try:
        resultado = RedeSocial.query.all()
        lista = []
        for item in resultado:
            lista.append(RedeSocial.to_json(item))
        return make_response(jsonify(lista), 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/redesocial/<int:id>', methods=['GET'])
def get_redesocialbyid(id):
    try:
        redesocial = RedeSocial.query.get_or_404(id)
        if (redesocial):
            rs = jsonify(redesocial.to_json())
        else:
            rs = jsonify({})
        return make_response(rs, 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/redesocial/', methods=['POST'])
def new_redesocial():
    try:
        resultado = RedeSocial().from_json(request.json)
        db.session.add(resultado)
        db.session.commit()
        if (resultado):
            rs = jsonify(resultado.to_json())
        else:
            rs = jsonify({})
        return make_response(rs, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/redesocial/', methods=['PUT'])
def update_redesocial():
    try:
        redesocial_alterado = RedeSocial().from_json(request.json)
        redesocial = RedeSocial.query.get(redesocial_alterado.id)
        redesocial.from_json(request.json)
        db.session.commit()
        return make_response(redesocial, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/redesocial/<int:id>', methods=['DELETE'])
def remove_redesocial(id):
    try:
        resultado = RedeSocial.query.get_or_404(id)
        db.session.delete(resultado)
        db.session.commit()
        return make_response("Removido com sucesso!", 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)

# Metodos do Grupo Usuario


@app.route('/grupousuario/', methods=['GET'])
def get_grupousuario():
    try:
        resultado = GrupoUsuario.query.all()
        lista = []
        for item in resultado:
            lista.append(GrupoUsuario.to_json(item))
            return make_response(jsonify(lista), 200)
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/grupousuario/', methods=['POST'])
def new_grupousuario():
    try:
        resultado = GrupoUsuario().from_json(request.json)
        db.session.add(resultado)
        db.session.commit()
        if (resultado):
            rs = jsonify(resultado.to_json())
        else:
            rs = jsonify({})
        return make_response(rs, 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


@app.route('/grupousuario/<int:usuario_id>/<int:grupo_id>/<int:tipo_usuario_id>', methods=['DELETE'])
def remove_grupousuario(usuario_id, grupo_id, tipo_usuario_id):
    try:
        resultado = GrupoUsuario.query.filter_by(usuario_id=usuario_id, grupo_id=grupo_id, tipo_usuario_id=tipo_usuario_id).first()
        db.session.delete(resultado)
        db.session.commit()
        return make_response("Removido com sucesso!", 200)
    except exc.IntegrityError as e:
        print(e)
        db.session.remove()
        pass
        return make_response(jsonify({}), 400)


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
    app.run(debug=True, host="0.0.0.0")

