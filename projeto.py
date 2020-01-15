"""

xyz = 1  # type int
print(xyz)

# using concatenation
print("valor: ", xyz)
print("valor " + str(xyz))

# using strings
car1, car2 = 'BMW-X6-ABC-X7',"VM"
car3 = "abcdefghijk"
car4 = "abcdefghijk"
print(car1)
print(car2)

xyz = 1.0  # type float
xyz = 1j  # type complex


# string
print()
print(car1[0:3])
print(car1[3:])

print(car1[::5])
print(car3[:5:3])

text1 = "curso de python básico\n" \
        "testando o codigo"
print(len(text1))
print(text1.upper())
print(text1.title())


# conditions
if (car1 == car2) :
    print("iguais")
else:
    print("diferente")

if (car3 == car4) :
    print("iguais")
else:
    print("diferente")

y = 1
car1 = "1"
if (car1==y):
    print("1 igual a '1'")

controle=';'
novoTexto=controle.join(text1)
print(novoTexto)

print(car1.isalnum())

print(text1.find("python"))
print(text1.rfind("python"))
print(text1[::-1].capitalize())

print(text1.swapcase())


# input from user

nome =  input("Qual seu nome?")
idade = int(input("Digite a sua idade!!!!!!!!!! "))

saidaIdade = "A idade {0} é de {1}"
print("Sua idade é: ",idade)
print(saidaIdade.format(idade,nome))


if (idade <= 15):
    print("Vc nao pode brincar no parquinho")
else:
    print("Voce precisa de autorização do pais")

def soma(a , b):
    print()
    return a + b

print(soma(1,2))
cont = 1
while (cont <=100):
    if (cont % 2 ==0):
        print("Contador :", cont)
    cont+=1

for cont in range (1,5):
    print("Pos{0} atual: ",format(cont) )

for cont in "Parabens":
    print("Pos{0} atual: ",format(cont) )


# Do while
i = 1
while True:
    print(i)
    i = i + 1
    if(i > 3):
        break

# List
list1=["Abc", "xyz", "klm"]

list2 = list(list1)
list2.append("LOP")
list1.remove("xyz")
#list1.clear()
list1.sort(reverse=True)

print(list2)
print(list1)

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)


# Tuplas
tupla = ("Andrea", "Fran", "Bianca", 1, list1)
print(tupla)


print(tupla[0].replace("Andrea", "GeeksforGeeks"))
print(tupla)

for cont in range (1,5):
    print("Pos{0} atual: ",format(cont) )



valor = "*"
for nome in range (0,4) :
    print(valor , end = ' ')
print()

for nome in range (1,3) :
    print(valor +"     "+ valor)

for nome in range (0,4) :
    print(valor , end = ' ')

for nome in range (0,6) :
    print(valor*nome)

space = ""
for s in range(0,5):
    space +=" "

#for nome in range(0,5):
#    if(nome % 2==0):
#        print(valor*nome)
iterador=0
for i in range (5, 0, -1):
    iterador = iterador+ 1
    print (' '*i + '*'*iterador)

# conjunto

conjunto1 = {"A", "B", "C"}
conjunto2 = {"X", "Y", "Z"}

# |& - ^
print(conjunto1 | conjunto2)
conj = conjunto1 & conjunto2
print(conj)
print(conjunto1 - conjunto2)

print(conjunto1 ^ conjunto2)

#class02
#dicionario
dict1 = {"produto" : "biscoito", "marca":"vitarella", "peso" : 90}

for d in dict1:
    print(d)

for d in dict1:
    print(dict1[d])

#item pertence ao dicionario
if "marca" in dict1:
    print("tem marca")

if "marcador" not in dict1:
    print("nao tem marcador")

for d in dict1.values():
    print("valores dic: ",d)

for d, v in dict1.items():
    print("chaves e valores:",d,v)


#acionando um item no dic
dict1["embalagem"]="plastica"
print(dict1)

#remove o ult
dict1.pop("embalagem")
print(dict1)

#substituicao do item adicionado
dict1["embalagem"] ="plastica"
dict1["embalagem"] ="tecido"
print(dict1)


#dict.popitem()
#del dict1["embalagem"]
#dict1.clear()
print(dict1)


#copy no dicionario

dict2 = dict1
dict3 = dict1.copy()

print(dict3)

aluno01 = {"matricula" : "2020001",
           "nome" : "Matheus",
           "idade" : 20 }

aluno02 = {"matricula" : "2020002",
           "nome" : "Tatiane",
           "idade" : 30}

aluno03 = {"matricula" : "2020003",
           "nome" : "Andressa",
           "idade" : 27 }


matriculados = {"aluno01" : aluno01, "aluno02" : aluno02, "aluno03" :aluno03}


print()
for mats in matriculados:
    print(matriculados[mats])
    #print(matriculados)

print()
for matsKey, matsValue in matriculados.items():
    print(matsKey, matsValue)
    for mat, val in matsValue.items():
        print(mat, val)



# Declaring a None variable
var = None

if var is None: # Checking if the variable is None
  print("None")
else:
  print("Not None")

  """
# function
def fatorial(n):
    pass


def mediaPonderada(*n):
    media =0
    quant =0
    for x in n:
        media = media +x
        qnt = qnt+1
    return media / quant

#Passando chaves como parametros
def carros(**car):
    print ("O carro eh: ", car["gm"], "o outro eh: ", car["fiat"])

carros(gm = "Onix", fiat="Uno")

x = lambda a, b: (a *b)
print("Multiplicacao com Lambda", x(6,5))

def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a, b):
    return a/b

def raizQuadrada(raiz):
    return raiz ** (1/2)

def main():
    print(soma(1,1))
    print(subtracao(1, 1))
    print(multiplicacao(1, 1))
    print("Div",divisao(1, 1))
    print("Raiz %d" % raizQuadrada(625))

if __name__ == "__main__":
    main()
