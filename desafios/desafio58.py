import random
n = 0
print('adivinhe o número que estou pensando de 1 a 10!')
a = random.randint(1, 10)
while n != a:
    n = int(input('Digite um número: '))
    if (n==a):
        print(f'Você venceu! O número era {n}!')
    else:
        print(f'Não é {n}! tente novamente!')