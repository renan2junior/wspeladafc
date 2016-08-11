import unittest

from flask import json

from app import app


class GrupoUsuarioApiTest(unittest.TestCase):

    lista = [{
              'ativo': True,
              'grupo_id': 1,
              'usuario_id': 1}
             ]

    def setUp(self):
        """Set up a blank temp database before each test"""
        self.app = app.test_client()

    def get_grupo_usuario(self):
        rs = self.app.get('/grupousuario/', follow_redirects=True)
        return rs

    def test_retorna_lista_grupo_usuario(self):
        self.assertIsNotNone('Lista vazia', self.get_grupo_usuario())

    def test_popula_grupo_usuario(self):
        for item in self.lista:
            print("grupo ===> %s" % item)
            res = self.app.post('/grupousuario/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def teste_remove_grupo_usuario(self):
        for item in json.loads(self.get_grupo_usuario().data):
            res = self.app.delete('/grupousuario/%s/%s' % (item['usuario_id'], item['grupo_id']), follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")


if __name__ == '__main__':
    unittest.main()