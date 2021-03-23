qtd = 0
while qtd <= 0:
    qtd = int(input('Voce quer informar quantos numeros? '))
    if qtd <= 0:
        print('A quantidade deve ser positiva')

soma = 0
for i in range(0, qtd):
    numero = 1001
    while numero > 1000:
        numero = int(input('Informe um numero: '))
        if numero > 1000:
            print('O numero deve ser menor ou igual a 1000!')
    if ('maior' not in vars()) or (numero > maior):
        maior = numero

    if ('menor' not in vars()) or (numero < menor):
        menor = numero

    soma += numero

print(f'Menor numero: {menor}')
print(f'Maior numero: {maior}')
print(f'Soma dos numeros: {soma}')
