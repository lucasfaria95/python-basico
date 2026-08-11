import random
alunos = []
for i in range(4):
    alunos.append(input(f"Digite o nome do aluno {i+1}: "))
escolhido = random.sample(alunos, 1)
ordem_apresentacao = random.sample(alunos, len(alunos))
print(f"A ordem de apresentação do trabalho será: {ordem_apresentacao}")