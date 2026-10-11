n = 0
numeros = []
sun = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    numeros.append(n)
    sun += n
print(f'Foram digitados {len(numeros)} valores e a soma entre eles é {sun}!')