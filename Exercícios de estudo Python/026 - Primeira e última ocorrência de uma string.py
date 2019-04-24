frase = str (input("digite uma frase: ")).lower().strip()
print ("voçê repetiu a letra {} vezes".format(frase.count("a")))
print("a primeira vez que a letra A apareceu foi na posição: {}".format(frase.find("a")+1))
print("a ultima vez que A apareceu foi: {}".format(frase.rfind("a")+1))