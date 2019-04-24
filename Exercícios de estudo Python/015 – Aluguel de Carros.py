dias = int (input("Quantos dias você ficou com o carro?:"))
km = float (input("Quantos Km você rodou?"))

v = (dias *60) + (km * 0.15)
print ("valor é {:.2f}".format(v))