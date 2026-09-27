soma = 0
cont = 0
for c in range(1, 500, 2):
    if (c % 3 == 0):
        soma += c
        cont += 1
print(f'O valor da soma de todos os {cont} multiplos de 3 do intervalo entre 1 e 500 é {soma}!')