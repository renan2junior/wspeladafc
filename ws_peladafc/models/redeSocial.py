from util.dbutil import db, ValidationError


class RedeSocial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(120), unique=True)

    def __init__(self, descricao):
        self.descricao = descricao

    def __init__(self):
        return

    def __repr__(self):
        return '<RedeSocial %r >' % self.descricao

    def to_json(self):
        return {
            'id': self.id,
            'descricao':self.descricao
        }

    def from_json(self, json):
        try:
            if json['id']:
                self.id = json['id']
            self.descricao = json['descricao']
        except KeyError as e:
            raise ValidationError('Rede Social insvalida !' + e.args[0])
        return self

