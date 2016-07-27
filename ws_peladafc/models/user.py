from util.dbutil import db, ValidationError


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __init__(self):
        return

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    def from_json(self, json):
        try:
            self.username = json['username']
            self.email = json['email']
        except KeyError as e:
            raise ValidationError('Usuario invalido : missing ' + e.args[0])
        return self
