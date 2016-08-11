from util.dbutil import db, ValidationError


class Pagamento(db.Model):
    mes = db.Column(db.String(6), primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'), primary_key=True)
    #usuario = db.relationship('Usuario', backref=db.backref('post', lazy='dynamic'))
    grupo = db.relationship('Grupo', backref=db.backref('post', lazy='dynamic'))

    def __init__(self):
        return

    def __repr__(self):
        return '<Pagamento $r>' % self.mes

    def to_json(self):
        return{
            'id': self.mes,
            'usuario_id': self.usuario_id,
            'grupo_id': self.grupo_id,
            'nome_grupo': self.grupo.nome_grupo
        }

    def from_json(self, json):
        try:
            self.mes = json['mes']
            self.usuario_id = json['usuario_id']
            self.grupo_id = json['grupo_id']
        except KeyError as e:
            raise ValidationError('Mes invalido ' + e.args[0])
        return self

