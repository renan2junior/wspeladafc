from util.dbutil import db, ValidationError


class Pagamento(db.Model):
    mes_ano = db.Column(db.String(6), primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'), primary_key=True)
    data_pagamento = db.Column(db.DateTime)
    valor_pago = db.Column(db.Float)

    def __init__(self):
        return

    def __repr__(self):
        return '<Pagamento $r>' % self.mes_ano

    def to_json(self):
        return{
            'mes_ano': self.mes_ano,
            'data_pagamento': self.data_pagamento,
            'valor_pago': self.valor_pago,
            'usuario_id': self.usuario_id,
            'grupo_id': self.grupo_id,
        }

    def from_json(self, json):
        try:
            self.mes_ano = json['mes_ano']
            self.usuario_id = json['usuario_id']
            self.grupo_id = json['grupo_id']
            self.valor_pago = json['valor_pago']
            self.data_pagamento = json['data_pagamento']
        except KeyError as e:
            raise ValidationError('Pagamento invalido ! ' + e.args[0])
        return self

