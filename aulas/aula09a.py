frase = 'curso em video python'
print(frase[9:21])  # Exibe a palavra 'python'
print(frase[:5])    # Exibe a palavra 'curso'
print(frase[6:13])  # Exibe a palavra 'em video'
print(frase[1::2])  # Exibe a frase pulando de 2 em 2 caracteres, começando do índice 1
print(frase.capitalize())  # Exibe a frase com a primeira letra maiúscula
print(frase.upper())  # Exibe a frase toda em maiúsculas
print(frase.lower())  # Exibe a frase toda em minúsculas
print(frase.strip())  # Exibe a frase sem espaços no início e no final
print(frase.replace('python', 'Java'))  # Substitui a palavra 'python' por 'Java'
print('curso' in frase)  # Verifica se a palavra 'curso' está na frase
print('''Hello, World!
This is a multi-line string.''')  # Exibe uma string de múltiplas linhas
print(frase.split())  # Divide a frase em uma lista de palavras
print('-'.join(frase))  # Junta os caracteres da frase com '-' entre eles
print(frase.count('o'))  # Conta quantas vezes a letra 'o' aparece na frase
print(frase.find('video'))  # Retorna o índice da primeira ocorrência da palavra 'video'
print(frase.index('python'))  # Retorna o índice da primeira ocorrência da palavra 'python'
print(frase.isalpha())  # Verifica se todos os caracteres da frase são letras
print(frase.isnumeric())  # Verifica se todos os caracteres da frase são números
print(frase.startswith('curso'))  # Verifica se a frase começa com 'curso'
print(frase.endswith('python'))  # Verifica se a frase termina com 'python'
print(frase.replace(' ', '_'))  # Substitui os espaços por underscores
print(frase.title())  # Exibe a frase com a primeira letra de cada palavra em maiúscula
print(frase.swapcase())  # Inverte o caso das letras na frase
print(frase.center(30))  # Centraliza a frase em um espaço de 30 caracteres
print(frase.ljust(30))  # Alinha a frase à esquerda em um espaço de 30 caracteres
print(frase.rjust(30))  # Alinha a frase à direita em um espaço de 30 caracteres
print(frase.zfill(30))  # Preenche a frase com zeros à esquerda até completar 30 caracteres
print(frase.encode())  # Codifica a frase em bytes
print(frase.islower())  # Verifica se todos os caracteres da frase estão em minúsculas
print(frase.isupper())  # Verifica se todos os caracteres da frase estão em maiúsculas
print(frase.istitle())  # Verifica se a frase está em formato de título
print(frase.isprintable())  # Verifica se todos os caracteres da frase são imprimíveis
print(frase.isascii())  # Verifica se todos os caracteres da frase são ASCII
print(frase.isidentifier())  # Verifica se a frase é um identificador válido
print(frase.isdecimal())  # Verifica se todos os caracteres da frase são decimais
print(frase.isdigit())  # Verifica se todos os caracteres da frase são dígitos
print(frase.isnumeric())  # Verifica se todos os caracteres da frase são numéricos
print(frase.isalnum())  # Verifica se todos os caracteres da frase são alfanuméricos
print(frase.isspace())  # Verifica se todos os caracteres da frase são espaços
print(len(frase))  # Retorna o comprimento da frase