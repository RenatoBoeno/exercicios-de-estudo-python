#Programa para aprovação de credito para financiamento de imóvel.

print("Olá, bem vindo a nossa central de financiamentos! Nós vamos pedir alguns dados.")
nome = str(input("Qual o seu nome? ")).upper()
casa = float(input("Valor da casa? R$ "))
salario = float(input("Qual o seu salario? R$ "))
anos = int(input("Você pretende pagar em quantos anos? "))

#calculo de credito

prestação = (casa / (anos *12))
minimo = salario * 30 / 100

print( "Olá {} , o valor da sua prestação é R$:{:.2f} ".format(nome,prestação), end='')

if   prestação <= minimo:
    print("Seu empréstimo foi APROVADO!")

else:
    print("Infelizmente não é possível continuar com sua solicitação de empréstimo.")