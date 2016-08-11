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