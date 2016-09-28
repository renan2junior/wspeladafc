from util.dbutil import db, ValidationError


class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_contato = db.Column(db.String(80), unique=False)
    email_contato = db.Column(db.String(120), unique=False)
    nome_grupo = db.Column(db.String(256), unique=True)
    horario = db.Column(db.String(256), unique=False)
    telefone_grupo = db.Column(db.String(256), unique=False)
    conta_grupo = db.Column(db.String(256), unique=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=False)
    usuario = db.relationship('Usuario', backref=db.backref('post', lazy='dynamic', cascade='all,delete'))
    local_id = db.Column(db.Integer, db.ForeignKey('local.id'), unique=False)
    local = db.relationship('Local', backref=db.backref('post', lazy='dynamic', cascade='all,delete'))

    def __init__(self, nome_contato, email_contato, local, nome_grupo, horario,
                 telefone_grupo, conta_grupo, usuario_id, local_id):
        self.nome_contato = nome_contato
        self.email_contato = email_contato
        self.local = local
        self.nome_grupo = nome_grupo
        self.horario = horario
        self.telefone_grupo = telefone_grupo
        self.conta_grupo = conta_grupo
        self.usuario_id = usuario_id
        self.local_id = local_id

    def __init__(self):
        return

    def to_json(self):
        return{
            'id': self.id,
            'nome_contato': self.nome_contato,
            'email_contato': self.email_contato,
            'nome_grupo': self.nome_grupo,
            'horario': self.horario,
            'telefone_grupo': self.telefone_grupo,
            'conta_grupo': self.conta_grupo,
            'usuario_id': self.usuario_id,
            'local_id': self.local_id
        }

    def from_json(self, json):
        try:
            if json['id']:
                self.id = json['id']
            self.nome_contato = json['nome_contato']
            self.email_contato = json['email_contato']
            self.nome_grupo = json['nome_grupo']
            self.horario = json['horario']
            self.telefone_grupo = json['telefone_grupo']
            self.conta_grupo = json['conta_grupo']
            self.usuario_id = json['usuario_id']
            self.local_id = json['local_id']
        except KeyError as e:
            raise ValidationError('Grupo invalida : missing ' + e.args[0])
        return self
