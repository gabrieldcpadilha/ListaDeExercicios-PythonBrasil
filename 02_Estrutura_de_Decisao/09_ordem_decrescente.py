# 09 - Faça um Programa que leia três números e mostre-os em ordem decrescente.


a = float(input('Informe um número: '))
b = float(input('Informe outro número: '))
c = float(input('Informe mais um número: '))

if a >= b >= c and a >= c:
    print(f'A ordem decrescente é {a} , {b} e {c}')
elif a >= b and a >= c >= b:
    print(f'A ordem decrescente é {a} , {c} e {b}')
elif b >= a >= c and b >= c:
    print(f'A ordem decrescente é {b} , {a} e {c}')
elif b >= a and b >= c >= a:
    print(f'A ordem decrescente é {b} , {c} e {a}')
elif c >= a >= b and c >= b:
    print(f'A ordem decrescente é {c} , {a} e {b}')
elif c >= a and c >= b >= a:
    print(f'A ordem decrescente é {c} , {b} e {a}')

""" EXEMPLO SIMPLES USANDO LISTA (Menos linhas de codigo)
lista = []
qtd = 3
for i in range(qtd):
    numero = int(input('Informe um numero: '))
    lista.append(numero)

lista.sort(reverse = True) //ordena os elementos
print(lista)
"""