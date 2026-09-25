num = int(input('Digite um número inteiro: '))
# Verifica se o número é menor ou igual a 1
if num <= 1:
    print(f'O número {num} não é primo.')
else:
    # Assume que o número é primo
    bool_primo = True
    # Testa a divisão de 2 até um número anterior ao escolhido
    for i in range(2, num):
        print(f'{i}')
        if num % i == 0:
            bool_primo = False
            break  # Encontra um divisor e para o loop
    if bool_primo:
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} não é primo.')
