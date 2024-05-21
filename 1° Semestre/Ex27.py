candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Ana"
}

total_votos_candidatos = {candidato: 0 for candidato in candidatos}
total_votos_nulos = 0
total_votos_em_branco = 0
total_votos = 0

while True:
    voto = int(input("Digite o código do candidato (ou 0 para encerrar a votação): "))

    if voto == 0:
        break

    if voto in candidatos:
        total_votos_candidatos[voto] += 1
    elif voto == 5:
        total_votos_nulos += 1
    elif voto == 6:
        total_votos_em_branco += 1
    else:
        print("Código inválido. Tente novamente.")

    total_votos += 1

print("\nResultado da Eleição:")
print("========================================")

# Total de votos para cada candidato
for candidato, votos in total_votos_candidatos.items():
    print(f"Total de votos para {candidatos[candidato]}: {votos}")

print("Total de votos nulos:", total_votos_nulos)
print("Total de votos em branco:", total_votos_em_branco)

# Percentagem de votos nulos e em branco sobre o total de votos
percentagem_nulos = (total_votos_nulos / total_votos) * 100
percentagem_brancos = (total_votos_em_branco / total_votos) * 100

print("Percentagem de votos nulos sobre o total de votos:", f"{percentagem_nulos:.2f}%")
print("Percentagem de votos em branco sobre o total de votos:", f"{percentagem_brancos:.2f}%")

print("========================================")
