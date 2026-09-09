primeira_nota = float(input('Qual a primeira nota do aluno: '))
segunda_nota = float(input('Qual a segunda nota do aluno: '))
media = (primeira_nota + segunda_nota) / 2

if media >= 7.0 and media <= 10:
    print(f'Sua mêdia é {media}. Parabéns! Você está aprovado!')
elif media >= 5 and media <= 6.9:
    print(f'Sua mêdia é {media}. Você está em recuperação!')
elif media < 5:
    print(f'Sua mêdia é {media}. Você está em reprovado!')
else:
    print(f'você inseriu valores invalidos!')