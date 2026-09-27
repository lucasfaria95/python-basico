#todos os números pares que estão entre 1 e o valor digitado
valor = int(input('Digite um número: '))

print(f'Estes são todos os números pares entre 1 e {valor}!')

for c in range(0, valor + 1, 2):
    print(f'{c}')
