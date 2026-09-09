pri_numero = int(input('digite um número: '))
seg_numero = int(input('digite outro número: '))

if pri_numero > seg_numero:
    print('O primeiro valor é maior!')
elif pri_numero < seg_numero:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')