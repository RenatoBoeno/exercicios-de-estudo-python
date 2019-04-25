umero = int(input('Digite um número: '))
flag = 0
for c in range(1, numero+1):
    if numero % c == 0:
        flag = flag + 1
if flag == 2:
    print('PRIMO')
else:
    print('NÃO PRIMO')
