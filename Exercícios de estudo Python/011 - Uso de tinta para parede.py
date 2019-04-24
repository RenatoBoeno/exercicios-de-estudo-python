larg = float (input("largura da parede: "))
alt = float (input ("altura da parede"))

area = larg*alt

print ("sua parede tem a dimensão de {}x{} e sua área é de {}n²".format(larg,alt,area))

tinta = area / 2

print ("tinta necessaria {}L de tinta".format(tinta))