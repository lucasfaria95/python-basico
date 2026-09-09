nome = str(input('Qual o seu nome? '))
if nome == 'Lucas':
    print(f'Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Tiago':
    print('Seu nome é bem pupolar no Brasil!')
elif nome in 'Caroline Ana Cláudia Jéssica Juliana':
    print('belo nome feminino!')
else:
    print(f'Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}!')