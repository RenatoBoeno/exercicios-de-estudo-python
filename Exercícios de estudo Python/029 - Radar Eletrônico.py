velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print("Voçê está acima do limite e foi multado.")
    multa = (velocidade -80) * 7
    print("valor da multa R${:.2f}".format(multa))
print("Bom dia, Dirija com segurança!")



