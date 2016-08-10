import unittest

from flask import json

from app import app


class TddInApp(unittest.TestCase):

    lista_tipo_usuario = ['Administrador','Jogador','Neutro']
    lista_usuario = ['Renan','Arthur']
    lista_times = ['Flamengo', 'Botafogo', 'Gremio']

    def setUp(self):
        """Set up a blank temp database before each test"""
        self.app = app.test_client()

    ## TIPO USUARIO

    def get_tipo_usuario(self):
        rs = self.app.get('/tipousuario/', follow_redirects=True)
        return rs

    def test_retorna_lista_tipo_usuario(self):
        self.assertIsNotNone('Lista vazia', self.get_tipo_usuario())

    def test_popula_tipo_usuario(self):
        for item in self.lista_tipo_usuario:
            res = self.app.post('/tipousuario/', data=json.dumps({"descricao":item}), content_type='application/json', follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def teste_remove_tipo_usuario(self):
        for item in json.loads(self.get_tipo_usuario().data):
            res = self.app.delete('/tipousuario/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")

    ## TIMES

    def get_time(self):
        rs = self.app.get('/time/', follow_redirects=True)
        return rs

    def test_retorna_lista_time(self):
        self.assertIsNotNone('Lista vazia', self.get_time())

    def test_popula_time(self):
        for item in self.lista_times:
            res = self.app.post('/time/', data=json.dumps({"nome": item}), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def teste_remove_time(self):
        for item in json.loads(self.get_time().data):
            res = self.app.delete('/time/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")


if __name__ == '__main__':
    unittest.main()