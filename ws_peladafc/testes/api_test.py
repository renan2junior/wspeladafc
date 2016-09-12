import unittest
from flask import json
from testes.massa_dados import MassaDados
from app import app
from util.dbutil import db


class ApiTest(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test"""
        self.app = app.test_client()

    def get_time(self):
        rs = self.app.get('/time/', follow_redirects=True)
        return rs

    def get_grupo(self):
        rs = self.app.get('/grupo/', follow_redirects=True)
        return rs

    def get_grupo_usuario(self):
        rs = self.app.get('/grupousuario/', follow_redirects=True)
        return rs

    def get_local(self):
        rs = self.app.get('/local/', follow_redirects=True)
        return rs

    def get_redesocial(self):
        rs = self.app.get('/redesocial/', follow_redirects=True)
        return rs

    def get_tipo_usuario(self):
        rs = self.app.get('/tipousuario/', follow_redirects=True)
        return rs

    def get_usuario(self):
        rs = self.app.get('/usuario/', follow_redirects=True)
        return rs

    def get_pagamentos(self):
        rs = self.app.get('/pagamento/', follow_redirects=True)
        return rs

    # REMOVER TODOS OS DADOS PELA API

    def test_stepA0_remove_pagamentos(self):
        for item in json.loads(self.get_pagamentos().data):
            res = self.app.delete(
                '/pagamento/%s/%s/%s' % (item['usuario_id'], item['grupo_id'], item['mes_ano']),
                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")

    def test_stepA1_remove_grupo_usuario(self):
        for item in json.loads(self.get_grupo_usuario().data):
            res = self.app.delete('/grupousuario/%s/%s/%s' % (item['usuario_id'], item['grupo_id'], item['tipo_usuario_id']), follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")

    def test_stepA2_remove_grupo(self):
        for item in json.loads(self.get_grupo().data):
            res = self.app.delete('/grupo/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")
        db.session.execute('truncate table grupo cascade;')
        db.session.execute('ALTER SEQUENCE grupo_id_seq  RESTART WITH 1;')

    def test_stepA3_remove_local(self):
        for item in json.loads(self.get_local().data):
            res = self.app.delete('/local/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")
        db.session.execute('truncate table local cascade;')
        db.session.execute('ALTER SEQUENCE local_id_seq  RESTART WITH 1;')

    def test_stepA4_remove_usuario(self):
        for item in json.loads(self.get_usuario().data):
            res = self.app.delete('/usuario/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")
        db.session.execute('truncate table usuario cascade;')
        db.session.execute('ALTER SEQUENCE usuario_id_seq  RESTART WITH 1;')

    def test_stepA5_remove_time(self):
        for item in json.loads(self.get_time().data):
            res = self.app.delete('/time/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")
        db.session.execute('truncate table time cascade;')
        db.session.execute('ALTER SEQUENCE time_id_seq  RESTART WITH 1;')

    def test_stepA6_remove_redesocial(self):
        for item in json.loads(self.get_redesocial().data):
            res = self.app.delete('/redesocial/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")

    def test_stepA7_remove_tipo_usuario(self):
        for item in json.loads(self.get_tipo_usuario().data):
            res = self.app.delete('/tipousuario/%s' % item['id'], follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, não foi possivel remover o item.")
        db.session.execute('truncate table tipo_usuario cascade;')
        db.session.execute('ALTER SEQUENCE tipo_usuario_id_seq  RESTART WITH 1;')

    # POPULAR TODOS OS DADOS PELA API

    def test_stepB1_popula_time(self):
        for item in MassaDados.listaTimes:
            res = self.app.post('/time/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def test_stepB2_popula_tipo_usuario(self):
        for item in MassaDados.listaTipousuario:
            res = self.app.post('/tipousuario/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def test_stepB3_popula_redesocial(self):
        for item in MassaDados.listaRedesocial:
            res = self.app.post('/redesocial/', data=json.dumps(item), content_type='application/json', follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def test_stepB4_popula_usuario(self):
        for item in MassaDados.listaUsuario:
            res = self.app.post('/usuario/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def test_stepB5_popula_local(self):
        for item in MassaDados.listaLocal:
            res = self.app.post('/local/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def test_stepB6_popula_grupo(self):
        for item in MassaDados.listaGrupo:
            res = self.app.post('/grupo/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def test_stepB7_popula_grupo_usuario(self):
        for item in MassaDados.listaGrupoUsuario:
            res = self.app.post('/grupousuario/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    def test_stepB8_popula_pagamento(self):
        for item in MassaDados.lista_pagamentos:
            res = self.app.post('/pagamento/', data=json.dumps(item), content_type='application/json',
                                follow_redirects=True)
            self.assertEqual(200, res.status_code, "Erro, inclusao sem sucesso!")

    # LISTA TODOS OS DADOS PELA API

    def test_stepC1_retorna_lista_grupo(self):
        self.assertIsNotNone('Lista vazia', self.get_grupo())

    def test_stepC2_retorna_lista_grupo_usuario(self):
        self.assertIsNotNone('Lista vazia', self.get_grupo_usuario())

    def test_stepC3_retorna_lista_local(self):
        self.assertIsNotNone('Lista vazia', self.get_local())

    def test_stepC4_retorna_lista_redesocial(self):
        self.assertIsNotNone('Lista vazia', self.get_redesocial())

    def test_stepC5_retorna_lista_time(self):
        self.assertIsNotNone('Lista vazia', self.get_time())

    def test_stepC6_retorna_lista_tipo_usuario(self):
        self.assertIsNotNone('Lista vazia', self.get_tipo_usuario())

    def test_stepC7_retorna_lista_usuario(self):
        self.assertIsNotNone('Lista vazia', self.get_usuario())

    def test_stepC8_retorna_lista_pagamento(self):
        self.assertIsNotNone('Lista vazia', self.get_pagamentos())


if __name__ == '__main__':
    unittest.main()