<<<<<<< HEAD
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
=======
import unittest

from flask import json

from app import app


class UsuarioApiTest(unittest.TestCase):

    lista = [{
              'nome':'Renan',
              'email':'renan2junior@gmail.com',
              'telefone': '3333-9999',
              'time_id':'1',
              'mensalista':'True',
              'horario':'11hs',
              'telefone':'3333-9999',
              'tipo_usuario_id':'1'},
                {
                'nome': 'Renan',
                'email': 'renan2junior@gmail.com',
                'telefone': '3333-9999',
                'time_id': '1',
                'mensalista': 'True',
                'horario': '11hs',
                'telefone': '3333-9999',
                'tipo_usuario_id': '1'}
    ]

    def setUp(self):
        """Set up a blank temp database before each test"""
        self.app = app.test_client()

    def get_usuario(self):
        rs = self.app.get('/usuario/', follow_redirects=True)
        return rs

    def test_retorna_lista_usuario(self):
        self.assertIsNotNone('Lista vazia', self.get_usuario())

    def test_popula_usuario(self):
        for item in self.lista:
            print("usuario ===> %s" % item)
            res = self.app.post('/usuario/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def teste_remove_usuario(self):
        for item in json.loads(self.get_usuario().data):
            res = self.app.delete('/usuario/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")


if __name__ == '__main__':
    unittest.main()
>>>>>>> df9515c2234cf684791e31398a06c88fd85a39ff
