from util.dbutil import db, ValidationError


class Pelada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_contato = db.Column(db.String(80), unique=False)
    email_contato = db.Column(db.String(120), unique=False)
    nome_pelada = db.Column(db.String(256), unique=True)
    horario_pelada = db.Column(db.String(256), unique=False)
    telefone_pelada = db.Column(db.String(256), unique=False)
    conta_pelada = db.Column(db.String(256), unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False)
    user = db.relationship('User', backref=db.backref('post', lazy='dynamic'))
    campo_id = db.Column(db.Integer, db.ForeignKey('campo.id'), unique=False)
    campo = db.relationship('Campo', backref=db.backref('post', lazy='dynamic'))

    def __init__(self, nome_contato, email_contato, local_pelada, nome_pelada, horario_pelada,
                 telefone_pelada, conta_pelada, user_id, campo_id):
        self.nome_contato = nome_contato
        self.email_contato = email_contato
        self.local_pelada = local_pelada
        self.nome_pelada = nome_pelada
        self.horario_pelada = horario_pelada
        self.telefone_pelada = telefone_pelada
        self.conta_pelada = conta_pelada
        self.user_id = user_id
        self.campo_id = campo_id

    def __init__(self):
        return

    def to_json(self):
        return{
            'id': self.id,
            'nome_contato': self.nome_contato,
            'email_contato': self.email_contato,
            'local_pelada': self.local_pelada,
            'nome_pelada': self.nome_pelada,
            'horario_pelada': self.horario_pelada,
            'telefone_pelada': self.telefone_pelada,
            'conta_pelada': self.conta_pelada,
            'user_id': self.user_id,
            'user': self.user.username,
            'campo_id': self.campo_id,
            'campo': self.campo.nome
        }

    def from_json(self, json):
        try:
            self.nome_contato = json['nome_contato']
            self.email_contato = json['email_contato']
            self.local_pelada = json['local_pelada']
            self.nome_pelada = json['nome_pelada']
            self.horario_pelada = json['horario_pelada']
            self.telefone_pelada = json['telefone_pelada']
            self.conta_pelada = json['conta_pelada']
            self.user_id = json['user_id']
            self.campo_id = json['campo_id']
        except KeyError as e:
            raise ValidationError('Pelada invalida : missing ' + e.args[0])
        return self
