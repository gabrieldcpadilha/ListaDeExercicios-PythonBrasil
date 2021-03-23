populacaoA = 80000
crescimentoA = 1.03
populacaoB = 200000
crescimentoB = 1.015

anos = 1
while populacaoA <= populacaoB:
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    anos += 1

print(f'Serao necessarios {anos} anos para que a populacao do pais A ultrapasse a populacao do pais B')
