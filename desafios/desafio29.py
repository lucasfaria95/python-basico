velocidade = int(input('digite a quantos Km/h estava o carro: '))
multa = 7
valmulta = (velocidade - 80) * multa

if (multa > 80):
    print(f'você foi multado(a) em {valmulta}')