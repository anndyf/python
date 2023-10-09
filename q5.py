# Cria listas vazias para armazenar os números e os números pares/ímpares
numeros = []
pares = []
impares = []

# Pede ao usuário para inserir 20 números inteiros
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Separa os números pares e ímpares
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Mostra os três vetores na tela
print("Números inseridos:")
print(numeros)

print("Números pares:")
print(pares)

print("Números ímpares:")
print(impares)
