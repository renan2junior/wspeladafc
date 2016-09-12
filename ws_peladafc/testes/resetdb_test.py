from unittest import TestCase
from models.grupo import Grupo
from models.grupoUsuario import GrupoUsuario
from models.local import Local
from models.pagamento import Pagamento
from models.redeSocial import RedeSocial
from models.time import Time
from models.tipoUsuario import TipoUsuario
from models.usuario import Usuario
from testes.massa_dados import MassaDados
from util.dbutil import db
from sqlalchemy import exc


class ResetdbTest(TestCase):

    def setUp(self):
        return

    def test_step0(self):
        try:
            db.reflect()
            db.drop_all()
        except exc.SQLAlchemyError as e:
            print(e)
            db.session.remove()
            pass

        try:
            db.create_all()
        except exc.SQLAlchemyError as e:
            print(e)
            db.session.remove()
            pass

    def test_step1_popula_times(self):

        i = 1
        for item in MassaDados.listaTimes:
            try:
                obj = Time().from_json(item)
                db.session.add(obj)
                db.session.commit()
                self.assertEqual(i, obj.id)
                i += 1
            except exc.IntegrityError as e:
                print(e)
                db.session.remove()
                pass

    def test_step2_popula_RedeSocial(self):
        i = 1
        for item in MassaDados.listaRedesocial:
            try:
                obj = RedeSocial().from_json(item)
                db.session.add(obj)
                db.session.commit()
                self.assertEqual(i, obj.id)
                i += 1
            except exc.IntegrityError as e:
                print(e)
                db.session.remove()
                pass

    def test_step3_popula_listaLocal(self):
        i = 1
        for item in MassaDados.listaLocal:
            try:
                obj = Local().from_json(item)
                db.session.add(obj)
                db.session.commit()
                self.assertEqual(i, obj.id)
                i += 1
            except exc.IntegrityError as e:
                print(e)
                db.session.remove()
                pass

    def test_step4_popula_tipousuario(self):
        i = 1
        for item in MassaDados.listaTipousuario:
            try:
                obj = TipoUsuario().from_json(item)
                db.session.add(obj)
                db.session.commit()
                self.assertEqual(i, obj.id)
                i += 1
            except exc.IntegrityError as e:
                print(e)
                db.session.remove()
                pass

    def test_step5_popula_listaUsuario(self):
        i = 1
        for item in MassaDados.listaUsuario:
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

    def test_step6_popula_listaGrupo(self):
        i = 1
        for item in MassaDados.listaGrupo:
            try:
                obj = Grupo().from_json(item)
                db.session.add(obj)
                db.session.commit()
                self.assertEqual(i, obj.id)
                i += 1
            except exc.IntegrityError as e:
                print(e)
                db.session.remove()
                pass

    def test_step7_popula_listaGrupoUsuario(self):
        i = 1
        for item in MassaDados.listaGrupoUsuario:
            try:
                obj = GrupoUsuario().from_json(item)
                db.session.add(obj)
                db.session.commit()
                i += 1
            except exc.IntegrityError as e:
                print(e)
                db.session.remove()
                pass

    def test_step8_popula_listaPagamentos(self):
        i = 1
        for item in MassaDados.lista_pagamentos:
            try:
                obj = Pagamento().from_json(item)
                db.session.add(obj)
                db.session.commit()
                i += 1
            except exc.IntegrityError as e:
                print(e)
                db.session.remove()
                pass