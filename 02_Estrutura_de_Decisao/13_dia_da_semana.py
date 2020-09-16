# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
# e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


numero_dia = int(input('Informe um numero para saber o dia da semana (1 a 7): '))

if numero_dia == 1:
    print('Domingo')
elif numero_dia == 2:
    print('Segunda-Feira')
elif numero_dia == 3:
    print('Terca-Feira')
elif numero_dia == 4:
    print('Quarta-Feira')
elif numero_dia == 5:
    print('Quinta-Feira')
elif numero_dia == 6:
    print('Sexta-Feira')
elif numero_dia == 7:
    print('Sabado')
else:
    print('Valor inválido')
