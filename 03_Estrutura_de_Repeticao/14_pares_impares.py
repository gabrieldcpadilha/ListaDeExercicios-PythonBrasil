par = 0
impar = 0

for c in range(1, 11):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Qtd numeros pares: {par}')
print(f'Qtd numeros impares: {impar}')
