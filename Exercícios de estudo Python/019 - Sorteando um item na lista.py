import  random

n1 = str (input("nome:"))
n2 = str (input("segundo aluno"))
n3 = str (input("terceiro nome"))
lista = [n1,n2,n3]

escolhido = random.choice(lista)

print ("aluno escolhido{}".format(escolhido))