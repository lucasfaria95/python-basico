quant_mais_18 = 0
quant_homens = 0
mulher_menos_20 = 0

while True:
    idade = 0
    sexo = ''
    continuar = ''

    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    while idade <=0:
        idade = int(input('Idade: '))
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo [M/F]'))
    print('-'*30)

    if idade >= 18:
        quant_mais_18 += 1
    if sexo == 'M':
        quant_homens += 1
    if  idade <= 20 and sexo == 'F':
        mulher_menos_20 += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar [S/N]'))
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {quant_mais_18}.')
print(f'Ao todo temos {quant_homens} homens cadastrados.')
print(f'E temos {mulher_menos_20} mulhres com menos de 20 anos.')   
