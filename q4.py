# Cria uma lista vazia para armazenar os caracteres
caracteres = []

# Pede ao usuário para inserir 10 caracteres
for i in range(10):
    caractere = input(f"Digite o {i+1}º caractere: ")
    caracteres.append(caractere)

# Define uma lista de consoantes
consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# Inicializa uma variável para contar as consoantes
contagem_consoantes = 0

# Lista para armazenar as consoantes lidas
consoantes_lidas = []

# Verifica cada caractere e conta as consoantes
for caractere in caracteres:
    if caractere in consoantes:
        contagem_consoantes += 1
        consoantes_lidas.append(caractere)

# Mostra as consoantes e a contagem na tela
print("Consoantes lidas:")
for consoante in consoantes_lidas:
    print(consoante)

print(f"Total de consoantes lidas: {contagem_consoantes}")
