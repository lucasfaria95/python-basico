from datetime import date
print('Qual o ano de sua data de nacimento? ')
ano_nascimento = int(input("Digite apenas o ano em que nasceu: "))
data_atual = date.today()
ano_atual = int(data_atual.year)
idade = int(ano_atual - ano_nascimento)
if idade <= 17:
    print(f'Você tem ou vai fazer {idade} anos, e falta {18-idade} anos para você se alistar ao serviço militar.')
elif idade >= 19:
    print(f'Você tem ou vai fazer {idade} anos, e passou {idade-18} anos do tempo para você se alistar ao serviço militar.')
else:
    print(f'É hora de você se alistar ao serviço militar!')