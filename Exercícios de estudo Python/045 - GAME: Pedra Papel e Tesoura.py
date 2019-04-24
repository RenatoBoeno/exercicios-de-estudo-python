
from random import randint
from time import sleep
nome = str (input("Qual o seu nome? ")).upper()
print("=="*25)
print(" "*3,"{}, VAMOS JOGAR PEDRA, PAPEL E TESOURA!!".format(nome))
print("=="*25)
print('''Suas opções 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
itens = ("PEDRA","PAPEL","TESOURA")
computador = randint(0, 2)
jogador = int(input("Qual é a sua jogada? "))
print ("PEDRA")
sleep(0.5)
print("PAPEL")
sleep(1)
print("TESOURA")
sleep(1)
print("-="*25)
print("Computador jogou {}".format(itens[computador]))
print("{} JOGOU {}".format(nome,itens[jogador]))
print("-="*25)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("{} Venceu".format(nome))
    elif jogador == 2:
        print("Computador venceu")
    else:
        print("Jogada inválida!")

elif computador == 1: #computador jogou papel
    if jogador == 0:
        print("Computador venceu")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("{} venceu".format(nome))
    else:
        print("Jogada inválida!")

elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print("{} venceu".format())
    elif jogador == 1:
        print("Computador venceu")
    elif jogador == 2:
        print("Empate")
    else:
        print("Jogada inválida!")
print("-="*25)
