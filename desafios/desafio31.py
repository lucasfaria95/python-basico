viagem = int(input('Qual a distância da viagem?'))
if (viagem <= 200):
    passagem = viagem * 0,5
    print(f'O valor da sua passagem é R${passagem}')
else:
    passagem = viagem * 0,45
    print(f'O valor da sua passagem é R${passagem}')