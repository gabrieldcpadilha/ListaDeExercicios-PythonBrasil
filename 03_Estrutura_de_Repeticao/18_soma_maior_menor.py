qtd = 0

while qtd <= 0:
    qtd = int(input('Digite quantos numeros deseja: '))
    if qtd <= 0:
        print('Digite um valor positivo')

soma = 0
for n in range(0, qtd):
    num = int(input('Digite um numero: '))
    if 'maior' not in vars() or num > maior:
        maior = num

    if 'menor' not in vars() or num < menor:
        menor = num

    soma += num

print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')
print(f'A soma dos numeros foi: {soma}')
