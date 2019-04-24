nome = input("Qual seu nome:?")
real = float (input("quanto você tem em R$: "))
dolar = real / 3.27
euro = real /4.33
print("Olá,{},com R$ {:.2f} você compra US${:.2f}, €{:.2f}.".format(nome,real,dolar,euro))