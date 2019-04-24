a: int = int (input("Primeiro numero: "))
b = int (input("segundo numero: "))
c = int (input("Terceiro numero: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor numero é {} e o maior é {}".format(menor,maior))