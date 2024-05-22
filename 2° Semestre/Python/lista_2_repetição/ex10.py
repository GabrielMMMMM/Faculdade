
respostas_corretas = ["b", "a", "d"]

pontuacao = 0

for i in range(3):
    resposta_aluno = input(f"Resposta da Questão {i + 1}: ").lower() 
    if resposta_aluno == respostas_corretas[i]:
        pontuacao += 1


print(f"Total de pontos: {pontuacao}")
