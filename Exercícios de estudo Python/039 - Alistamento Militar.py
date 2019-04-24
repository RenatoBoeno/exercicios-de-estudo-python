from datetime import date
atual = date.today().year
nasc = int (input("Em que ano você nasceu? "))
sexo = int (input('''Qual seu sexo:
[1] Masculino 
[2] Feminino '''))

idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))


if sexo==1 and idade == 18:
     print("Voce precisa se alistar Imediatamente")

if sexo==1 and  idade < 18:
    saldo = 18 - idade
    print("Voce ainda nao precisa de alistar, faltam {} anos.".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}".format(ano))

if sexo==1 and  idade > 18:
    saldo = idade - 18
    print("Voce ja deveria ter se alistado há {} anos.".format(saldo))
    ano = atual - saldo
    print( "Seu alistamento foi em {}".format(ano))

elif sexo==2:
    print("Mulheres não sao obrigadas a se alistar.")