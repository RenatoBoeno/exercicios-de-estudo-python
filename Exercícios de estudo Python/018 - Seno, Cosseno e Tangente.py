import math
an = float(input("digite o angulo que deseja:"))
seno = math.sin(math.radians((an)))
print ("angulo{:.2f} seno {:.2f}".format(an,seno))
cosseno = math.cos(math.radians((an)))
print(" o angulo de {:.2f} tem o cosseno{:.2f}".format(an,cosseno))
tangente = math.tan(math.radians(an))
print(" o angulo é {:.2f} tem a tangente{:.2f}".format(an,tangente))