# Cria uma lista vazia para armazenar os números
numeros = []

# Pede ao usuário para inserir 5 números inteiros
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Mostra os números lidos
print("Os números digitados são:")
for numero in numeros:
    print(numero)
