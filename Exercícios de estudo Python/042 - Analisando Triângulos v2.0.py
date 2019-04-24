seg1: float = float(input("Digite o primeiro segmento: "))
seg2 = float(input("Digite o segundo segmento: "))
seg3 = float(input("Digite o terceiro segmento: "))
if seg1 < seg2 + seg3 and   seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("Os segmentos acima formam um triangulo", end=" ")
    if seg1 == seg2 == seg3:
     print("EQUILÁTERO")
    elif seg1 != seg2 != seg3 != seg1:
        print(" ESCALENO")
    else:
        print("ISÓSCELES")

else:
    print("Os segmentos acima não formam um triangulo")