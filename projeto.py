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
"""


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

for nome in range(0,5):
    if(nome % 2==0):
        print(valor*nome)

for i in range (5, 0, -1):
    iterador=1
    iterador = iterador+ i
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