from unittest import TestCase
from flask import json
from sqlalchemy import exc

from app import app
from util.dbutil import db

from models.usuario import Usuario

class UsuarioTest(TestCase):


    lista = [{

        'nome': 'Arthur',
        'email': 'arthur@gmail.com',
        'telefone': '1234567890',
        'mensalista': True,
        'time_id': 1,
        'tipo_usuario_id': 1},
        {

        'nome': 'Renan',
        'email': 'renan@gmail.com',
        'telefone': '0987654321',
        'mensalista': True,
        'time_id': 1,
        'tipo_usuario_id': 1
        }
    ]


    def setUp(self):
        db.session.execute('truncate table usuario cascade;')
        db.session.execute('ALTER SEQUENCE usuario_id_seq  RESTART WITH 1;')
        db.session.commit()
        return


    def test_create(self):
        i = 1
        for item in self.lista:
            try:
                obj = Usuario().from_json(item)
                db.session.add(obj)
                db.session.commit()
                self.assertEqual(i, obj.id)
                i += 1
            except exc.IntegrityError as e:
                print(e)
                db.session.remove()
                pass
