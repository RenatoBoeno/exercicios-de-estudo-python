num1 = int (input("Digite um numero inteiro"))
print( '''Escolha uma das bases para conversão
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')

opção =  int(input("sua opçao: "))

if opção == 1:
    print("{} convertido para bináio é igual a {}.".format(num1, bin(num1)[2:]))
elif opção == 2:
    print("{} convertido para octal é igual a {}".format(num1, oct(num1)[2:]))
elif opção == 3:
    print("{} convertido para haxadecimal é igual a {}".format(num1,hex(num1)[2:]))
else:
    print("Opção Invalida.")