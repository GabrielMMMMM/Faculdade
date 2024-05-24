def somaMatriz (matriz, linhas, colunas):
    soma = 0 
    for i in range(linhas):
        for j in range(colunas):
             soma += matriz[i][j]
    return soma

matriz = [[1, 2, 3],
          [1, 2, 3],
          [1, 2, 3]]

linhas = 3
colunas = 3

resultado = somaMatriz(matriz, linhas, colunas)

print(resultado)
