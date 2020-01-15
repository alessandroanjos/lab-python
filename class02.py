from Pessoa import *
from Servidor import Servidor
from Coordenador import Coordenador
from Sequencial import  Sequencial

p1 = Pessoa("João", 12)
#print(p1.get_credito())
p1.credito = True

print(p1.nome)
print(p1.idade)
print(p1.credito)

s1 = Servidor("Andressa", 27, 1313)

cord1 = Coordenador("Julio", 40, 458, "Inspetor")

print(s1.matricula)
print(cord1.funcao)

sequencia = Sequencial()
seqinterator = iter(sequencia)
print(next(seqinterator))
print(next(seqinterator))
