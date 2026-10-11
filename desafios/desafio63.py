n = int(input('Até que número da sequência de Fibonacci você deseja? '))
cont = 2
anterior = 0
atual = 1
prox = anterior + atual
print(anterior)
print(atual)
while cont != n:
    cont += 1
    prox = anterior + atual
    print(f'{prox}')
    anterior = atual
    atual = prox