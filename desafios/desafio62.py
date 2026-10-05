# Lê o primeiro termo e a razão da PA
primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
max_vezes = int(input('Digite quantos termos da razão da P.A. deseja mostrar: '))
resultado = primeiro
contador = 1

while max_vezes >= 1:
    while contador <= max_vezes:
        print(f'{resultado},')
        resultado += razao
        contador += 1
    max_vezes = int(input('Deseja mostrar mais quantos termos? '))
    contador = 1