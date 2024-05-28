def inverteMatriz(matriz, lar): 
    matriz.reverse()

    for i in range (0, lar):
        matriz[i].reverse()
    print(matriz)

matriz = [[1,2,3],
          [4,5,6], 
          [7,8,9]]    

inverteMatriz(matriz, 3) 