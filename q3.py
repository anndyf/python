# Cria uma lista vazia para armazenar as notas
notas = []

# Pede ao usuário para inserir as 4 notas
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Calcula a média das notas
media = sum(notas) / len(notas)

# Mostra as notas e a média na tela
print("Notas inseridas:")
for nota in notas:
    print(nota)

print(f"Média das notas: {media:.2f}")
