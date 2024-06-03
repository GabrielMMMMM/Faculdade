def mediaPonderaa(nota, peso):
    #calcula a parte de cima da formula
    a = 0
    for i in range (0, len(nota)):
        x = nota[i]*peso[i]
        a += x
    #calcula a media ponderada
    mediaponderada = a / sum(peso)
    print (mediaponderada)

nota = [1100, 2000, 5500, 12500]
peso = [5, 16, 3, 1]

mediaPonderaa(nota, peso)

#Formula: X = x1⋅p1+x2⋅p2+x3⋅p3+…/p1+p2+p3+…"


