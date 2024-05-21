num_cidades = 5
acidentes_transito = []
veiculos_passeio = []

for i in range(num_cidades):
    print(f"\nCidade {i+1}:")
    codigo_cidade = input("Código da cidade: ")
    num_veiculos = int(input("Número de veículos de passeio (em 1999): "))
    num_acidentes = int(input("Número de acidentes de trânsito com vítimas (em 1999): "))

    acidentes_transito.append(num_acidentes)
    veiculos_passeio.append(num_veiculos)


indice_max = max(acidentes_transito)
indice_min = min(acidentes_transito)
cidade_max = acidentes_transito.index(indice_max) + 1
cidade_min = acidentes_transito.index(indice_min) + 1

print("\nEstatísticas:")
print(f"Maior índice de acidentes de trânsito: {indice_max} (Cidade {cidade_max})")
print(f"Menor índice de acidentes de trânsito: {indice_min} (Cidade {cidade_min})")


media_veiculos = sum(veiculos_passeio) / num_cidades
print(f"Média de veículos nas cinco cidades: {media_veiculos}")

cidades_menos2000 = [acidentes_transito[i] for i in range(num_cidades) if veiculos_passeio[i] < 2000]
media_acidentes_menos2000 = sum(cidades_menos2000) / len(cidades_menos2000)
print(f"Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: {media_acidentes_menos2000}")
