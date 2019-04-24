import  random

n1 = str(input("primeiro aluno"))
n2 = str (input ("segundo nome"))
n3 =  str (input("terceiro nome"))

lista = [n1,n2,n3]

random.shuffle(lista)
print ("ordem de apresentação")
print (lista)
