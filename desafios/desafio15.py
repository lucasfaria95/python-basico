d = float(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos quilômetros foram percorridos: '))
preco = d * 60 + km * 0.15
print(f'O preço a pagar pelo aluguel do carro é R${preco:.2f}')