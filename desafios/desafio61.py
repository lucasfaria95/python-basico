# Lê o primeiro termo e a razão da PA
primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
resultado = razao
# Calcula o décimo termo usando a fórmula do termo geral
decimo = primeiro + (10 - 1) * razao
# Mostra os 10 primeiros termos
while resultado <= decimo:
    print(f'{resultado},')
    resultado += razao