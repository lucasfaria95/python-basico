nome_maior_idade = ''
mulheres_idade_menor = 0
soma_idades = 0
maior_idade_homem = 0 

for i in range (1,5,1):
    print(f'{i}º pessoa')
    nome = input(f'Digite o nome da {i}º pessoa: ')
    idade = int(input(f'Digite a idade da {i}º pessoa: '))
    sexo = input(f'Digite o sexo da {i}º pessoa: ')

    soma_idades += idade

    if maior_idade_homem <= idade and sexo == 'M':
        nome_maior_idade = nome
    elif idade < 20 and sexo == 'F':
        mulheres_idade_menor += 1

print(f'A média de idade do grupo é {soma_idades / 4} anos, o nome do homem mais velho é {nome_maior_idade} e {mulheres_idade_menor} mulheres tem menos de 20 anos!')