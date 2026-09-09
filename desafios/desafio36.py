valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu sálario? '))
anos = int(input('Em quantos anos você vai pagar? '))
meses = float(anos * 12)
pres_mensal = valor / meses
if pres_mensal <= valor/100*30:
    print(f'Crédito aprovado! Você pagará R${pres_mensal} em {meses} meses. Este valor corresponde a {pres_mensal/(salario/100)}% do seu salário!')
else:
    print(f'Crédito negado! Você pagaria R${pres_mensal} em {meses} meses. Este valor corresponde a {pres_mensal/(salario/100)}% do seu salário!')