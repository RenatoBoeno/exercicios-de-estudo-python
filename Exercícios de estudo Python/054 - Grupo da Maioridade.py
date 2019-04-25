from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor= 0
for pess in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu: ".format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totalmaior +=1
    else:
        totalmenor +=1
print("Ao todo {} pessoas são maiores de 18 anos e {} não são maiores de 18 anos.".format(totalmaior,totalmenor))
