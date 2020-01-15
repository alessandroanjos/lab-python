class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self._credito = True

    @property
    def credito(self):
        return self._credito

    @credito.setter
    def credito(self, valor):
        if (self.idade > 17):
            self._credito = valor
        else:
            self._credito = False




