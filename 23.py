while True:
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    idade = int(input("Digite sua idade (entre 0 e 150): "))
    salario = float(input("Digite seu salário (maior que zero): "))
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ")
    estado_civil = input("Digite seu estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ")
    
    if len(nome) > 3 and 0 <= idade <= 150 and salario > 0 and (sexo == 'f' or sexo == 'm') and (estado_civil in ['s', 'c', 'v', 'd']):
        break
    else:
        print("Alguma informação é inválida. Tente novamente.")
print("Informações válidas.")