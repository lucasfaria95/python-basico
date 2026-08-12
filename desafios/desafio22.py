nomecompleto = 'Lucas Fernando Soares Farias' #nome completo do usuário
maiusculo = nomecompleto.upper() #nomecompleto em letras maiúsculas
minusculo = nomecompleto.lower() #nomecompleto em letras minúsculas
quantas_letras = len(nomecompleto) - nomecompleto.count(" ") #nomecompleto sem contar os espaços
letras_primeiro_nome = nomecompleto.find(" ") #quantas letras tem o primeiro nome
print("Nome completo em maiúsculas:", maiusculo)
print("Nome completo em minúsculas:", minusculo)
print("Quantidade de letras no nome completo (sem espaços):", quantas_letras)
print("Quantidade de letras no primeiro nome:", letras_primeiro_nome)
