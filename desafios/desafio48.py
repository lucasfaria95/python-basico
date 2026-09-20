soma = 0
for c in range(1, 500):
    if (c % 3 == 0):
        soma = soma + c
print(f'O valor da soma de todos os multiplos de 3 do intervalo entre 1 e 500 é {soma}!')