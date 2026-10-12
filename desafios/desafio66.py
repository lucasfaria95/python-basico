n = 0
numeros = []
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999: break
    numeros.append(n)
print(f'Foram digitados {len(numeros)} valores e a soma entre eles é {sum(numeros)}!')