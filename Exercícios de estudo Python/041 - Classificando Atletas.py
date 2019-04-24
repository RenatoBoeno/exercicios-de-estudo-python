# classificar categoria de atleta através da idade

from datetime import date
atual = date.today().year
nascimento = int(input("Digite o ano em que nasceu: "))
idade = atual - nascimento
print(" Sua categoria é :")

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 25:
    print("Sênior")
elif idade > 25:
    print("Master")