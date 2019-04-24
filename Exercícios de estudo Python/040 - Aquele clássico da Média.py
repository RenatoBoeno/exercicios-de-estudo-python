nota1 = float(input("Digite a primeira nota: "))
nota2 = float (input("Digite a seunda nota: "))
media =  (nota1 + nota2) / 2

print("Sua nota é {:.2f}".format(media))

if media >= 7.0:
    print("Aprovado.")

elif media < 7 and media > 5:
    print("Recuperação.")
elif media < 5:
    print("Reprovado.")