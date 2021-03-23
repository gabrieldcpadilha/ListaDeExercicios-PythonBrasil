inicio = int(input('Informe um valor inicial: '))
fim = inicio

while fim <= inicio:
    fim = int(input('Informe o valor final: '))
    if fim <= inicio:
        print('O valor final deve ser maior que o valor inicial')

for n in range(inicio, fim + 1):
    print(n)
