from util.dbutil import db, ValidationError


class Pagamento(db.Model):
    mes = db.Column(db.String(6), primary_key=True)
    jogador_id = db.Column(db.Integer, db.ForeignKey('jogador.id'), primary_key=True)
    pelada_id = db.Column(db.Integer, db.ForeignKey('pelada.id'), primary_key=True)
    jogador = db.relationship('Jogador', backref=db.backref('post', lazy='dynamic'))
    pelada = db.relationship('Pelada', backref=db.backref('post', lazy='dynamic'))

    def __init__(self):
        return

    def __repr__(self):
        return '<Pagamento $r>' % self.mes

    def to_json(self):
        return{
            'id': self.mes,
            'jogador_id': self.jogador_id,
            'nome_jogador': self.jogador.nome,
            'pelada_id': self.pelada_id,
            'nome_pelada': self.pelada.nome_pelada
        }

    def from_json(self, json):
        try:
            self.mes = json['mes']
            self.jogador_id = json['jogador_id']
            self.pelada_id = json['pelada_id']
        except KeyError as e:
            raise ValidationError('Mes invalido ' + e.args[0])
        return self

