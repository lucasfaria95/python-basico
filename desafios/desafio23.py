numero = int(input("Digite um número inteiro de 0 a 9999: "))
if numero < 0 or numero > 9999:
    print("Número inválido! Digite um número entre 0 e 9999.")
else:
    unidade = numero // 1 % 10
    dezena = numero // 10 % 10
    centena = numero // 100 % 10
    milhar = numero // 1000 % 10
    print("Analisando o número:", numero)
    print("Unidade:", unidade)
    print("Dezena:", dezena)
    print("Centena:", centena)
    print("Milhar:", milhar)