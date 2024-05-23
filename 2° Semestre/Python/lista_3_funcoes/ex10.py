def conta_palavras():
    cont = 1
    for i in palavra:
        if i == " ":
            cont += 1
    print(f'Tem {cont} palavras na frase digitada.')        
palavra = str(input("Digite uma frase: "))
conta_palavras()
#acho que tem um jeito melhor de fazer!!!