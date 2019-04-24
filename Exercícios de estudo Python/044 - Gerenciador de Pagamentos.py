from time import sleep

print("=="*25)
print(" "*15,"NOME DA LOJA")
print("=="*25)
preço = float(input("Valor das compras R$: "))
print('''Formas de pagamento!
[1] à vista - Dinheiro / Débito
[2] à vista no cartão
[3] em até 2x no cartão de crédito
[4] 3x ou mais no cartão de crédito''')
opção = int(input("Qual a opção do pagamento? "))
sleep(0.5)
print("AGUARDE UM INSTANTE...")
sleep(1)
if opção == 1:
    total = preço -(preço *10 / 100)
    print("Utilizando essa opção você recebe desconto as compras de R$ {:.2f} irão custar R$ {:.2f}.".format(preço, total))
elif opção == 2:
    total = preço -(preço *5 /100)
    print("Utilizando essa opção você recebe desconto as compras de R$ {:.2f} irão custar R$ {:.2f}.".format(preço, total))
elif opção == 3:
    total = preço
    print("Ao utilizar essa opçao o valor da compra não sofre alteração, o valor a ser pago é {:.2f}".format(total))
elif opção == 4:
    parcelas = int(input("Em quantas vezes deseja parcelar? "))
    total = preço + (preço *20 / 100)
    print("Utilizando a opção de parcelamento em {} vezes vai custar {}x de R$:{:.2f}, o total será R${:.2f"
          "}".format(parcelas,parcelas,total/ parcelas, total))
else:
    print("Opção inválida")


