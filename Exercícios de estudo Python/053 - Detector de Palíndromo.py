texto = str(input("Digite uma frase: ")).strip()
junto = texto.upper().replace(' ','')
inverso = ''
for c in range (len(junto) - 1, -1, -1):
    inverso = inverso + junto[c]
print ("O inverso de {} é {}.".format(junto, inverso))
if inverso == junto:
    print ("Temos um PALÍNDROMO!")
else:
    print ("A frase digitada NÃO é um PALÍNDROMO.")
