while True:
    nome_ginasta = input("Nome do ginasta: ")
    if not nome_ginasta:
        break

    notas = []
    for i in range(7):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    # Remover a melhor e a pior nota
    melhor_nota = max(notas)
    pior_nota = min(notas)
    notas.remove(melhor_nota)
    notas.remove(pior_nota)

    media = sum(notas) / len(notas)

    print("\nResultado final:")
    print(f"Atleta: {nome_ginasta}")
    print("Melhor nota: {:.1f}".format(melhor_nota))
    print("Pior nota: {:.1f}".format(pior_nota))
    print("Média: {:.2f}".format(media))
    print()
