print("=="*20)
print(" "*3,"Olá, vamos calcular o seu imc.")
print("=="*20)
altura = float(input("Digite a sua altura: "))
peso = float(input("Agora digite o seu peso (Kg): "))
imc = peso / (altura **2)
print("Seu IMC é : {:.1f} e você está ".format(imc),end=" ")
if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 25:
    print("peso ideal")
elif imc <=30:
    print("com sobrepeso")
elif imc <= 40:
    print(" com obesidade")
elif imc >40:
    print("com obesidade mórbida")
