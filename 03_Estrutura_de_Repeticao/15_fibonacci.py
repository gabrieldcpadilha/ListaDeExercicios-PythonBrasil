termo = 0

while termo <= 0:
    termo = int(input('Qual o termo que deseja a serie de Fibonaci? '))
    if termo <= 0:
        print('O termo tem que ser positivo')

primeiro = 0
print(primeiro)
segundo = 1
for n in range(1, termo):
    print(segundo)
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro