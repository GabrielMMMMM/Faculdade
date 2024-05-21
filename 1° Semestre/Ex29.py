while True:
    nome_atleta = input("Nome do atleta: ")
    if not nome_atleta:
        break

    saltos = []
    for i in range(5):
        distancia_salto = float(input(f"{i+1}º Salto: "))
        saltos.append(distancia_salto)

    # Remover o melhor e o pior salto
    melhor_salto = max(saltos)
    pior_salto = min(saltos)
    saltos.remove(melhor_salto)
    saltos.remove(pior_salto)

    media_saltos = sum(saltos) / len(saltos)

    print("\nResultado final:")
    print(f"Atleta: {nome_atleta}")
    print("Melhor salto: {:.2f} m".format(melhor_salto))
    print("Pior salto: {:.2f} m".format(pior_salto))
    print("Média dos demais saltos: {:.2f} m".format(media_saltos))
    print()
