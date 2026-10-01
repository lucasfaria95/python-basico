valor_1 = 0
valor_2 = 0
opcao = ''
result = 0

while valor_1 == 0 and valor_2 == 0:
    valor_1 = float(input('Digite o 1º valor: '))
    valor_2 = float(input('Digite o 2º valor: '))

    opcao = int(input('''O que deseja fazer?
    [1] Somar
    [2] Multiplicar
    [3] Maior número
    [4] Digitar novos númneros
    [5] sair do programa
    '''))
    if opcao == 1:
        result = valor_1 + valor_2
        print(f'A soma entre {valor_1} e {valor_2} é {result}!')
    elif opcao == 2:
        result = valor_1 * valor_2
        print(f'A multiplicação entre {valor_1} e {valor_2} é {result}!')
    elif opcao == 3:
        result = max(valor_1, valor_2)
        print(f'O maior valor entre {valor_1} e {valor_2} é {result}!')
    elif opcao == 4:
        valor_1 = valor_2 = 0
    elif opcao == 5:
        print('''Saindo...
                 Até a próxima!''')
    else:
        valor_1 = valor_2 = 0
        print(f'Opção {opcao} inválida!')