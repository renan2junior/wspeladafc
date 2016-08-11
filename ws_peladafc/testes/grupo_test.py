import unittest

from flask import json

from app import app


class GrupoApiTest(unittest.TestCase):

    lista = [{
              'nome_contato':'Renan',
              'email_contato':'renan2junior@gmail.com',
              'local_id':'5',
              'nome_grupo':'CICM',
              'horario':'11hs',
              'telefone_grupo':'3333-9999',
              'usuario_id':'1',
              'conta_grupo':'AG 102-4 CC 33456-0'},
             ]

    def setUp(self):
        """Set up a blank temp database before each test"""
        self.app = app.test_client()

    def get_grupo(self):
        rs = self.app.get('/grupo/', follow_redirects=True)
        return rs

    def test_retorna_lista_grupo(self):
        self.assertIsNotNone('Lista vazia', self.get_grupo())

    def test_popula_grupo(self):
        for item in self.lista:
            print("grupo ===> %s" % item)
            res = self.app.post('/grupo/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def teste_remove_grupo(self):
        for item in json.loads(self.get_grupo().data):
            res = self.app.delete('/grupo/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")


if __name__ == '__main__':
    unittest.main()