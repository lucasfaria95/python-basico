import random
parImpar = ''
venceu = 0

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    num = int(input('diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] '))
    ran = random.randint(1,2) 
    print(f'Você jogou {num} e o computador jogou {ran}. Total de {num + ran}')
    if (((ran + num) % 2 == 0) and pi == 'P'):
        print('-'*30)
        print(f'Você jogou {num} e o computador jogou {ran}. Total de {num + ran} DEU PAR')
        print('-'*30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
        venceu += 1
    elif (((ran + num) % 2 != 0) and pi == 'I'):
        print('-'*30)
        print(f'Você jogou {num} e o computador jogou {ran}. Total de {num + ran} DEU ÍMPAR')
        print('-'*30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
        venceu += 1
    elif(((ran + num) % 2 != 0) and pi == 'P'):
        print('-'*30)
        print(f'Você jogou {num} e o computador jogou {ran}. Total de {num + ran} DEU ÍMPAR')
        print('-'*30)
        print('Você PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! você venceu {venceu} vezes.')
        break
    elif(((ran + num) % 2 == 0) and pi == 'I'):
        print('-'*30)
        print(f'Você jogou {num} e o computador jogou {ran}. Total de {num + ran} DEU PAR')
        print('-'*30)
        print('Você PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! você venceu {venceu} vezes.')
        break