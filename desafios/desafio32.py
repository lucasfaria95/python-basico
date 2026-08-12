ano = int(input('digite um ano: ')):
if (ano % 4 == 0 and ano >1000):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')

if (ano >=1000 and ano % 400 == 0 and ano.endswith(00)):
    print(f'o ano {ano} é bissexto!')
else:
    Print(f'O ano {ano} não bissexto!')