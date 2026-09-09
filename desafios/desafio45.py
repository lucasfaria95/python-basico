from random import choice
jokenpo = [ 'pedra', 'papel', 'tesoura' ]

print('JOKENPÔ')
print("""escolha uma das opções a baixo:
1 - Pedra!
2 - Papel!
3 - Tesoura!""")
opcao = int(input('Qual opcao deseja?'))
player = jokenpo[opcao-1]
aleatorio = choice(jokenpo)

print(f'Você escolheu {player} e eu escolhi {aleatorio}!]')
# Empate
if player == aleatorio:
    print('O resultado é: EMPATE!')
# vitória do Jogador
elif (player == 'pedra' and aleatorio == 'tesoura') or (player == 'tesoura' and aleatorio == 'papel') or (player =='papel' and aleatorio == 'pedra'):
    print('O resultado é: VOCÊ VENCEU!')
# vitória da máquina    
elif (aleatorio == 'pedra' and player == 'tesoura') or (aleatorio == 'tesoura' and player == 'papel') or (aleatorio =='papel' and player == 'pedra'):
    print('O resultado é: VOCÊ PERDEU!')
# Se o Player escolher uma opção inválida
else:
    print('opção inválida!')