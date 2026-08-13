velocidade = int(input('digite a quantos Km/h estava o carro: '))
multa = 7
valmulta = (velocidade - 80) * multa

if (velocidade > 80):
    print(f'você foi multado(a) em R${valmulta:.2f}')
else:
    print('você não foi multado(a)')