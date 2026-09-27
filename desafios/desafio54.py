from datetime import date

# Pega a data atual
hoje = date.today()

# Extrai apenas o ano
ano_atual = hoje.year

maiores = []
menores = []

for i in range (1,8,1):
    ano_nacs = int(input(f'Digite o ano de nascimento da pessoa {i}: '))
    if ano_atual - ano_nacs >= 18:
        maiores.append(ano_nacs)
        print(f'Esta pessoa é maior de idade e tem {ano_atual - ano_nacs} anos!')
    elif ano_atual -ano_nacs <= 18 and ano_atual - ano_nacs >= 0:
        menores.append(ano_nacs)
        print(f'Esta pessoa é menor de idade e tem {ano_atual - ano_nacs} anos!')
    else:
        print(f'O ano digitado é inválido!')

quant_maiores = len(maiores)
quant_menores = len(menores)

print (f'{quant_maiores} pessoas são maiores de idades e {quant_menores} pessoas são menores de idade!')