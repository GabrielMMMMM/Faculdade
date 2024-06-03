def calculaMediaMatriz(matriz, linhas, colunas):
    # Verifica se a matriz não está vazia
    if not matriz:
        return 0
    
    soma = 0
    elementos = 0

    # Percorre a matriz e soma todos os elementos
    for i in range(linhas):
        for j in range(colunas):
            soma += matriz[i][j]
            elementos += 1

    # Calcula a média
    media = soma / elementos

    return media

# Exemplo de uso:
matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
linhas_exemplo = 3
colunas_exemplo = 3

media = calculaMediaMatriz(matriz_exemplo, linhas_exemplo, colunas_exemplo)
print(f'A média da matriz é: {media}')
