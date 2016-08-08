from util.dbutil import db, ValidationError


class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True)
    endereco = db.Column(db.String(256), unique=False)
    nome_contato = db.Column(db.String(80), unique=False)
    email_contato = db.Column(db.String(120), unique=False)
    telefone_contato = db.Column(db.String(256), unique=False)
    conta_deposito = db.Column(db.String(120), unique=False)

    def __init__(self, nome, endereco, nome_contato, email_contato,
                 telefone_contato, conta_deposito):
        self.nome = nome
        self.endereco = endereco
        self.nome_contato = nome_contato
        self.email_contato = email_contato
        self.telefone_contato = telefone_contato
        self.conta_deposito = conta_deposito

    def __init__(self):
        return

    def __repr__(self):
        return '<Local %r>' % self.nome

    def to_jason(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'nome_contato': self.nome_contato,
            'email_contato': self.email_contato,
            'telefone_contato': self.telefone_contato,
            'conta_deposito': self.conta_deposito
        }

    def from_json(self, json):
        try:
            self.nome = json['nome']
            self.endereco = json['endereco']
            self.nome_contato = json['nome_contato']
            self.email_contato = json['email_contato']
            self.telefone_contato = json['telefone_contato']
            self.conta_deposito = json['conta_deposito']
        except KeyError as e:
            raise ValidationError('Local invalido! ' + e.args[0])
        return self
