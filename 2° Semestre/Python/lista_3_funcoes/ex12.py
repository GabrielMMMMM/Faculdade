def contador_caractere():
    cont = 0
    for i in palavra:
        if i == caractere:
            cont+=1
    print (f"A letra {caractere} aparece {cont} vezes na palavra {palavra}.")        

palavra = str(input('Digite uma palavra: ')) 
caractere = str (input('Digite uma letra: '))
contador_caractere()   