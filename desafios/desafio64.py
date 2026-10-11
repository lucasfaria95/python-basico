n = 0
numeros = []
sun = 0
while n != 999:
    n = int(input('Digite um número: '))
    numeros.append(n)
    sun += n
print(f'Foram digitados {len(numeros)-1} e a soma entre eles é {sun-999}')
