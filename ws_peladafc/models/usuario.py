from util.dbutil import db, ValidationError


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    telefone = db.Column(db.String(12), unique=False)
    mensalista = db.Column(db.Boolean, unique=False)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'), unique=False)
    time = db.relationship('Time', backref=db.backref('post', lazy='dynamic', cascade='all,delete'))
    tipo_usuario_id = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id'), unique=False)
    tipo_usuario = db.relationship('TipoUsuario', backref=db.backref('post', lazy='dynamic',cascade='all,delete'))

    def __init__(self, nome, email, telefone, time, mensalista, time_id, tipo_usuario_id, tipo_usuario):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.time = time
        self.mensalista = mensalista
        self.time_id = time_id
        self.tipo_usuario_id = tipo_usuario_id
        self.tipo_usuario = tipo_usuario

    def __init__(self):
        return

    def __repr__(self):
        return '<Usuario %r>' % self.nome

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'mensalista': self.mensalista,
            'time': self.time.nome,
            'time': self.time.to_json(),
            'tipo_usuario': self.tipo_usuario.to_json()
        }

    def from_json(self, json):
        try:
            if json.get('id'):
               self.id = json['id']
            self.nome = json['nome']
            self.email = json['email']
            self.telefone = json['telefone']
            self.mensalista = json['mensalista']
            self.time_id = json['time_id']
            self.tipo_usuario_id = json['tipo_usuario_id']
        except KeyError as e:
            raise ValidationError('Usuario invalido : missing ' + e.args[0])
        return self
