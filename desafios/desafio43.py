altura = float(input('Insira sua altura em metros: '))
peso = float(input('insira seu peso em quilograma: '))

IMC = peso / (altura * altura)

if IMC < 18.5 and IMC > 0:
    print(f'Seu IMC é {IMC} e você está baixo do peso ideal.')
elif IMC >= 18.5 and IMC <=25:
    print(f'Seu IMC é {IMC} e você está com o peso ideal.')
elif IMC > 25 and IMC <= 30:
    print(f'Seu IMC é {IMC} e você está com sobrepeso.')
elif IMC > 30 and IMC <= 40:
    print(f'Seu IMC é {IMC} e você está com Obesidade.')
elif IMC > 40:
    print(f'Seu IMC é {IMC} e você está com Obesidade Mórbida.')
else:
    print('Os valores inseridos são invalidos!')