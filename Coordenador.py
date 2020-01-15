from Servidor import *


class Coordenador(Servidor):

    def __init__(self, nome, idade, matricula, funcao):
        super().__init__(nome, idade, matricula)
        self.funcao = funcao
