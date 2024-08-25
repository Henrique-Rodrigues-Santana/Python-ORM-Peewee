from peewee import *

db = SqliteDatabase("banco_de_dados.db")

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha =CharField()

    class Meta:
        database = db


class Anuncios(Model):
    usuario = ForeignKeyField(Usuario,backref='usuarios'),
    titulo = CharField()
    descricao = TextField()
    valor = DecimalField()
    
    class Meta:
        database = db


