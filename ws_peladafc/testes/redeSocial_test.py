import unittest

from flask import json

from app import app


class RedeSocialApiTest(unittest.TestCase):

    lista = ['Facebook', 'Gmail']

    def setUp(self):
        """Set up a blank temp database before each test"""
        self.app = app.test_client()

    def get_redesocial(self):
        rs = self.app.get('/redesocial/', follow_redirects=True)
        return rs

    def test_retorna_lista_redesocial(self):
        self.assertIsNotNone('Lista vazia', self.get_redesocial())

    def test_popula_redesocial(self):
        for item in self.lista:
            res = self.app.post('/redesocial/', data=json.dumps({"descricao":item}), content_type='application/json', follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def teste_remove_redesocial(self):
        for item in json.loads(self.get_redesocial().data):
            res = self.app.delete('/redesocial/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")


if __name__ == '__main__':
    unittest.main()