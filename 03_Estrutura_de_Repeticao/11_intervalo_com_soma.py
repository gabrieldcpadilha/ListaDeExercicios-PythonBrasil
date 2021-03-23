inicio = int(input('Informe o valor inicial: '))
fim = inicio

while fim <= inicio:
    fim = int(input('Informe o valor final: '))
    if fim <= inicio:
        print('O valor final deve ser maior que o valor inicial')

soma = 0

for n in range(inicio, fim + 1):
    soma += n
    print(n)

print(f'A soma dos numeros é: {soma}')
