cidade = input("Digite o nome de uma cidade: ")
cidade = cidade.strip()  # Remove espaços em branco no início e no final
if cidade[:5].lower() == "santo":
    print("A cidade começa com 'Santo'.")
else:
    print("A cidade não começa com 'Santo'.")