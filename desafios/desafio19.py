import random
alunos = []
for i in range(4):
    alunos.append(input(f"Digite o nome do aluno {i+1}: "))
escolhido = random.choice(alunos)
print(f"O aluno escolhido foi para apagar o quadro é: {escolhido}")