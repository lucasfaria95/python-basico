ano = int(input('digite um ano e descubra se é bissexto: '))
#if (ano % 4 == 0 and ano <1000):
#    print(f'O ano {ano} é bissexto!')

print(ano % 4 == 0 and ano < 1000) # testa se é bissexto e menor que 1000
print(ano % 400 == 0 and ano >= 1000 and str(ano).endswith('00')) # testa se é bissexto e maior que 1000 e termina com 00
print(ano % 4 == 0 and not str(ano).endswith('00') and ano % 400 != 0) # testa se é bissexto e não termina com 00 e não é divisível por 400

if (ano % 4 == 0 and ano < 1000) or (ano % 400 == 0 and ano >= 1000 and str(ano).endswith('00')) or (ano % 4 == 0 and not str(ano).endswith('00') and ano % 400 != 0):
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')