resposta = ''
n = 0
numeros = []
while resposta != 'N':
    n = int(input('Digite um número: '))
    numeros.append(n)
    resposta = str(input('Quer continuar? Digite "S" ou "N" '))
print(f'A média dos {len(numeros)} valores digitados é {sum(numeros) / len(numeros)}!')
print(f'O menor valor digitado foi {min(numeros)} e maior foi {max(numeros)}!')
print('Até a próxima!')