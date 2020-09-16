"""Faça um Programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:

    326 = 3 centenas, 2 dezenas e 6 unidades

    12 = 1 dezena e 2 unidades

    Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numero = int(input('Informe um numero inteiro: '))

centena = numero / 100
dezena = (numero - (centena * 100)) / 10
unidade = (numero - (centena * 100) - (dezena * 10))

saida = ''
if centena > 0:
    saida = saida + str(centena)
    if centena > 1:
        saida = saida + ' centenas '
    else:
        saida = saida + ' centena '

if dezena > 0:
    if unidade == 0 and centena != 0:
        saida = saida + 'e '
    saida = saida + str(dezena)
    if dezena > 1:
        saida = saida + ' dezenas '
    else:
        saida = saida + ' dezena '

if unidade > 0:
    if centena != 0 or dezena != 0:
        saida = saida + 'e '
    saida = saida + str(unidade)
    if unidade > 1:
        saida = saida + ' unidades'
    else:
        saida = saida + ' unidade'

print(saida)
