numero = int(input('digite um número: '))
print('Em qual base numerica você quer converte-lo?')
print('digite "1" para bínario')
print('digite "2" para octal')
print('digite "3" para hexadecimal')
opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    print(f'{numero} em bínario é igual a {bin(numero)}!')
elif opcao == 2:
    print(f'{numero} em octal é igual a {oct(numero)}!')
elif opcao == 3:
    print(f'{numero} em hexadecimal é igual a {hex(numero)}!')
else:
    print('Opção inválida!')