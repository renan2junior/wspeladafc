from util.dbutil import db, ValidationError


class RedeSocialUsuario(db.Model):
    identificador = db.Column(db.String(120), unique=False)
    usuario_id = db.Column(db.Integer, db.ForeingKey('usuatio_id'), primary_key=True)
    redesocial_id = db.Column(db.Integer, db.ForeingKey('redesocial_id'), primary_key=True)

    def __init__(self):
        return

    def to_json(self):
        return {
            'usuario_id': self.usuario_id,
            'redesocial_id': self.redesocial_id,
            'identificador': self.identificador
        }

    def from_json(self, json):
        try:
            self.identificador = json['identificador']
        except KeyError as e:
            raise ValidationError('Rede Social Usuario invalido! ' + e.args[0])
        return self
