idade = int(input('Qual a idade do atleta? '))

if idade <= 9 and idade >=1:
    print (f'Com {idade} anos a categoria é Mirim!')
elif idade > 9 and idade <= 14:
    print (f'Com {idade} anos a categoria é Infantil!')
elif idade > 14 and idade <= 19:
    print (f'Com {idade} anos a categoria é Junior!')
elif idade > 19 and idade <= 20:
    print (f'Com {idade} anos a categoria é Senior!')
elif idade > 20:
    print (f'Com {idade} anos a categoria é Master!')
else:
    print('A idade inserida é inválida!')