n = str (input("digite seu nome completo: ")).strip()
nome = n.split()
print("Olá: {} {}".format(nome[0],nome[len(nome)-1]))
