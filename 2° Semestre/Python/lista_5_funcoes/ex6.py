def contaCaracter(palavra, caracter):
    # Verifica quantas letras iguais tem na palavra
    cont = 0
    for i in palavra:
        if i == caracter:
            cont +=1
            
    print (f"A letra {caracter} aparece {cont} vezes na palavra {palavra}.")        

palavra = input("Digite uma palavra: ")
caracter = input ("Digite um caracter: ")

contaCaracter(palavra, caracter)