t = int(input('Digite o um número que deseja saber a tabuada: '))
print(f'A tabuada de {t} é:')
for c in range(1, 11):
    print(f'{t} x {c} = {t*c}')