# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

data = str(input('Informe uma data no formato dd/mm/yyyy: '))

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

bissexto = False
if ano % 4 == 0:
    bissexto = True
    if ano % 100 == 0 and ano % 400 != 0:
        bissexto = False

verifica = True
if mes in (1, 3, 5, 7, 8, 10, 12):
    if dia < 1 or dia > 31:
        verifica = False
elif mes in (4, 6, 9, 11):
    if dia < 1 or dia > 30:
        verifica = False
else:
    if bissexto:
        if dia < 1 or dia > 29:
            verifica = False
    else:
        if dia < 1 or dia > 28:
            verifica = False

if verifica:
    print(f'A data {data} é: VALIDA')
else:
    print(f'A data {data} é: INVÁLIDA')
