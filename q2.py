# Cria uma lista vazia para armazenar os números reais
numeros = []

# Pede ao usuário para inserir 10 números reais
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)

# Mostra os números na ordem inversa
print("Números na ordem inversa:")
for numero in reversed(numeros):
    print(numero)
