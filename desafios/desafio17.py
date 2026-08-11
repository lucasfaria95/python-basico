import math
catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')