dist= int(input("Digite a distancia a ser percorrida: "))
print("Você está prestes a começar uma viagem de {}Km".format(dist))

if dist <= 200:
    preço = dist*0.50
else:
    preço = dist*0.45
print("O valor da passagem é R$ {:.2f}".format(preço))