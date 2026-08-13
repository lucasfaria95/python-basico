import random

n = int(input('Digite um número: '))
a = random.randint(1, 5)

if (n==a):
    print('Você venceu!')
else:
    print('Você perdeu!')