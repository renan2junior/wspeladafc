from util.dbutil import db, ValidationError


class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    telefone = db.Column(db.String(12), unique=False)
    mensalista = db.Column(db.Boolean, unique=False)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'), unique=False)
    time = db.relationship('Time', backref=db.backref('post', lazy='dynamic'))

    def __init__(self, nome, email, telefone, time, mensalista, time_id):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.time = time
        self.mensalista = mensalista
        self.time_id = time_id

    def __init__(self):
        return

    def __repr__(self):
        return '<Jogador %r>' % self.nome

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'time_id': self.time_id,
            'mensalista': self.mensalista,
            'time': self.time.nome

        }

    def from_json(self, json):
        try:
            self.nome = json['nome']
            self.email = json['email']
            self.telefone = json['telefone']
            self.mensalista = json['mensalista']
            self.time_id = json['time_id']
        except KeyError as e:
            raise ValidationError('Jogador invalido : missing ' + e.args[0])
        return self
