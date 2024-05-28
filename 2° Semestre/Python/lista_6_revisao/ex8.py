def desvioPadrao(lista):

    numElementos = len(lista)
    somaElementos = sum(lista)

    media1 = somaElementos/numElementos
    lista2 = []

    for i in range (0, 5):
        n = (lista [i]-media1)**2
        lista2.append(n) 
    
    media2 = sum(lista2)/numElementos
    
    desvio_padrao = (media2 ** 1/2)
    print (desvio_padrao)


lista = [7, 9, 10, 11, 13]

print (f"O desvio padrão é: {desvioPadrao(lista)}")