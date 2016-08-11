from util.dbutil import db, ValidationError


class GrupoUsuario(db.Model):
    ativo = db.Column(db.Boolean)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=False, primary_key=True)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'), unique=False, primary_key=True)
    tipo_usuario_id = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id'), unique=False, primary_key=True)

    def __init__(self, ativo, grupo_id, usuario_id, tipo_usuario_id):
        self.ativo = ativo
        self.usuario_id = usuario_id
        self.grupo_id = grupo_id
        self.tipo_usuario_id = tipo_usuario_id

    def __init__(self):
        return

    def to_json(self):
        return{
            'ativo': self.ativo,
            'usuario_id': self.usuario_id,
            'grupo_id': self.grupo_id,
            'tipo_usuario_id': self.tipo_usuario_id
        }

    def from_json(self, json):
        try:
            self.ativo = json['ativo']
            self.usuario_id = json['usuario_id']
            self.grupo_id = json['grupo_id']
            self.tipo_usuario_id = json['tipo_usuario_id']

        except KeyError as e:
            raise ValidationError('Grupo Usuario invalido! : missing ' + e.args[0])
        return self
