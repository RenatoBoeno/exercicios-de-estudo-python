from random import randint
from time import sleep
pc = randint(0,5) #Faz o computador "pensar"
print("=="*30)
print(" "*10,"BEM VINDO AO JOGO DE ADIVINHAÇÃO!"," "*10)
print("Tente advinhar em qual numero estou pensando...entre 0 e 5")
print("=="*30)

jogador = int (input("Você sabe qual é o número? ")) #o jogador tenta adivinhar
print("Calma ai...")
sleep(3)
if jogador == pc:
    print("Acertou! Nossa você é o bichão mesmo ein!")
else:
    print("Errrrrow! tente de novo apertando f10")

