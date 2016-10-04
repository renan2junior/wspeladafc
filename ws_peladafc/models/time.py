from util.dbutil import db, ValidationError


class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True)

    def __init__(self, nome):
        self.nome = nome

    def __init__(self):
        return

    def __repr__(self):
        return '<Time %r>' % self.nome

    def to_json(self):
        return{
            'id': self.id,
            'nome': self.nome
        }

    def from_json(self, json):
        try:
            if json.get('id'):
                self.id = json['id']
            self.nome = json['nome']
        except KeyError as e:
            raise ValidationError('Time invalido !' + e.args[0])
        return self
