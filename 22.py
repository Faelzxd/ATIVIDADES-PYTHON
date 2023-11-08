while True:
    nome_usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    if nome_usuario != senha:
        break
    else:
        print("Erro: a senha não pode ser igual ao nome de usuário. Tente novamente.")
print("Nome de usuário e senha válidos.")