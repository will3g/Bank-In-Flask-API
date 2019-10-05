from database import db
from sqlalchemy import Column, Integer, String, Numeric

class Conta(db.Model):

    _id = Column('id', Integer(), primary_key=True)
    _numero = Column('numero', String(255), nullable=False, unique=True)
    _titular = Column('titular', String(255), nullable=False)
    _saldo = Column('saldo', Numeric(), nullable=False)
    _limite = Column('limite', Numeric(), nullable=False)

    def __init__(self, numero, titular, saldo, limite=1001.0, id=None):
        self._id = id
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def id(self):
        return self._id

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def titular(self):
        return self._titular.capitalize()

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def deposita(self, valor):
        self._saldo -= valor

    def saca(self, valor):
        self._saldo -= valor

    def transfere_para(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)

    def __str__(self):
        return 'Conta: [id: {}, numero: {}, titular: {}, saldo: {}, limite: {}]'\
            .format(self._id, self._numero, self._titular, self._saldo, self._limite)