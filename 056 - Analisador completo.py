somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ""
totalmulher20 = 0
for p in range (1,5):
    print("---- {}ª Pessoa".format(p))
    nome = str(input("Qual é seu nome? ")).strip().upper()
    idade = int(input("Qual e sua idade? "))
    sexo = str(input("Qual seu sexo? [M/F]")).strip().upper()
    somaidade += idade
    if p == 1 and sexo in "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "M" and idade > maioridadehomem:
        maioridadehomem =  idade
        nomevelho = nome
    if sexo in "F" and idade < 20:
        totalmulher20 += 1
médiaidade = somaidade / 4
print("A média de idade do grupo é {} anos.".format(médiaidade))
print("O homem mais velho tem {} anos e se chama {} ".format(maioridadehomem , nomevelho))
print("Ao todos são {} mulheres com menos de 20 anos.".format(totalmulher20))
