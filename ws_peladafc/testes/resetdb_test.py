from unittest import TestCase
from flask import json
from sqlalchemy import exc

from app import app
from util.dbutil import db

from models.usuario import Usuario

class ResetdbTest(TestCase):


    listaUsuario = [{
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

    listaTimes = [{'nome':'Flamengo'}, {'nome':'Botafogo'}, {'nome':'Gremio'}]

    listaTipousuario = [{'descricao': 'Administrador'}, {'descricao': 'Jogador'}, {'descricao': 'Neutro'}]

    listaRedesocial = [{'descricao': 'Facebook'}, {'descricao': 'Gmail'}]

    listaGrupo = [
        {
            'nome_contato':'Renan',
            'email_contato':'renan2junior@gmail.com',
            'local_id':'5',
            'nome_grupo':'CICM',
            'horario':'11hs',
            'telefone_grupo':'3333-9999',
            'usuario_id':'1',
            'conta_grupo':'AG 102-4 CC 33456-0'
        },
        {
            'nome_contato':'Renan',
            'email_contato':'renan2junior@gmail.com',
            'local_id':'5',
            'nome_grupo':'CICM',
            'horario':'11hs',
            'telefone_grupo':'3333-9999',
            'usuario_id':'1',
            'conta_grupo':'AG 102-4 CC 33456-0'
        }
    ]

    listaLocal = [{'id': '1',
              'nome': 'Campo Turano',
              'endereco': 'Rua Cardoso, Honorio Gurgel',
              'nome_contato': 'Roberto',
              'email_contato': 'rsj@gmail.com',
              'telefone_contato': '2220-3333',
              'conta_deposito': 'AG 102-4 CC 33456-0'},
             {'id': '2',
              'nome': 'Campo Lagoa',
              'endereco': 'Rua Barao, Lagoa',
              'nome_contato': 'Janete',
              'email_contato': 'faria@gmail.com',
              'telefone_contato': '4440-3333',
              'conta_deposito': 'AG 102-4 CC 33456-0'},
             {'id': '3',
              'nome': 'Campo Barra',
              'endereco': 'Av. das Americas, Barra',
              'nome_contato': 'Joana',
              'email_contato': 'joana@gmail.com',
              'telefone_contato': '5555-3333',
              'conta_deposito': 'AG 106-4 CC 3666-0'},
             {'id': '4',
              'nome': 'Campo Cascadura',
              'endereco': 'Rua Ernani Cardoso, Cascadura',
              'nome_contato': 'Paulo',
              'email_contato': 'paulo@gmail.com',
              'telefone_contato': '9999-3333',
              'conta_deposito': 'AG 203-4 CC 66456-0'}
             ]

    def setUp(self):
        db.session.execute('truncate table usuario cascade;')
        db.session.execute('ALTER SEQUENCE usuario_id_seq  RESTART WITH 1;')
        db.session.commit()
        return