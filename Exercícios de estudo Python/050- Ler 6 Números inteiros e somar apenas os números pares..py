soma = 0
cont = 0
for c in range(1, 7):
    num: int = int(input("Digite o {} valor: ".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você informou {} números e a soma deles foi {}".format(cont,soma))
