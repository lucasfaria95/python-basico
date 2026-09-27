peso = []

for i in range (1,3,1):
    peso_digitado = float(input(f'digite o peso da {1}º pessoa em Kg: '))
    peso.append(peso_digitado)

print(f'O peso máximo lido é {max(peso)} e o peso mínimo lido é {min(peso)}')