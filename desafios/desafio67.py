while True:
    num = int(input('quer ver a tabuada de qual valor? '))
    if num < 0: 
        print('PROGRAMA TABUADA ENCERRADO. volte sempre!')
        break
    print('-' *30)
    for i in range(1, 11):
        print(f'{num} X {i} = {num * i}')
    print('-' *30)