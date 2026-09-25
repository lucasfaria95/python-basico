texto = str(input('digite uma frase: '))
texto_invert = texto.replace(' ', '')[::-1]
if texto.replace(' ', '') == texto.replace(' ', '')[::-1]:
    print('A frase que você digitou é um palindromo!')
else:
    print('A frase que você digitou não é um palindromo!')