#todos os números pares que estão entre 1 e o valor digitado
valor = int(input('Digite um número: '))

print(f'Estes são todos os números pares entre 1 e {valor}!')

for c in range(1, valor + 1):
    if((c % 2 == 0) and valor > 0):
        print(f'{c} é par!')
