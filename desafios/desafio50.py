soma = 0

for c in range(6):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        soma = soma + valor
print(f'A soma dos números pares que você digitou é {soma}!')