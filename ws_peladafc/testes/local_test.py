import unittest

from flask import json

from app import app


class LocalApiTest(unittest.TestCase):

    lista = [{'nome':'Campo Turano',
              'endereco':'Rua Cardoso, Honorio Gurgel',
              'nome_contato':'Roberto',
              'email_contato':'rsj@gmail.com',
              'telefone_contato':'2220-3333',
              'conta_deposito':'AG 102-4 CC 33456-0'},
             {'nome': 'Campo Lagoa',
              'endereco': 'Rua Barao, Lagoa',
              'nome_contato': 'Janete',
              'email_contato': 'faria@gmail.com',
              'telefone_contato': '4440-3333',
              'conta_deposito': 'AG 102-4 CC 33456-0'},
             {'nome': 'Campo Barra',
              'endereco': 'Av. das Americas, Barra',
              'nome_contato': 'Joana',
              'email_contato': 'joana@gmail.com',
              'telefone_contato': '5555-3333',
              'conta_deposito': 'AG 106-4 CC 3666-0'},
             {'nome': 'Campo Cascadura',
              'endereco': 'Rua Ernani Cardoso, Cascadura',
              'nome_contato': 'Paulo',
              'email_contato': 'paulo@gmail.com',
              'telefone_contato': '9999-3333',
              'conta_deposito': 'AG 203-4 CC 66456-0'}
             ]

    def setUp(self):
        """Set up a blank temp database before each test"""
        self.app = app.test_client()

    def get_local(self):
        rs = self.app.get('/local/', follow_redirects=True)
        return rs

    def test_retorna_lista_local(self):
        self.assertIsNotNone('Lista vazia', self.get_local())

    def test_popula_local(self):
        for item in self.lista:
            print("LOCAL ===> %s" % item)
            res = self.app.post('/local/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def teste_remove_local(self):
        for item in json.loads(self.get_local().data):
            res = self.app.delete('/local/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")


if __name__ == '__main__':
    unittest.main()