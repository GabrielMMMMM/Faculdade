gabarito = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "E",
    7: "D",
    8: "C",
    9: "B",
    10: "A"
}

total_alunos = 0
total_acertos = []
soma_notas = 0

while True:
    respostas_aluno = {}
    acertos = 0

    # Captura as respostas do aluno
    for num_questao in range(1, 11):
        resposta = input(f"Digite a resposta da questão {num_questao}: ")
        respostas_aluno[num_questao] = resposta

    # Compara as respostas do aluno com o gabarito
    for num_questao, resposta_gabarito in gabarito.items():
        resposta_aluno = respostas_aluno[num_questao]

        if resposta_aluno == resposta_gabarito:
            acertos += 1

    # Atualiza as estatísticas
    total_alunos += 1
    total_acertos.append(acertos)
    soma_notas += acertos

    # Verifica se outro aluno vai utilizar o sistema
    resposta = input("Outro aluno vai utilizar o sistema? (S/N): ")
    if resposta.upper() != "S":
        break

# Resultados
maior_acerto = max(total_acertos)
menor_acerto = min(total_acertos)
media_notas = soma_notas / total_alunos

print("\nResultados:")
print("========================================")
print(f"Maior Acerto: {maior_acerto}")
print(f"Menor Acerto: {menor_acerto}")
print(f"Total de Alunos: {total_alunos}")
print(f"Média das Notas da Turma: {media_notas:.2f}")
print("Gabarito da Prova:")
for num_questao, resposta_gabarito in gabarito.items():
    print(f"{num_questao:02d} - {resposta_gabarito}")
print("========================================")
