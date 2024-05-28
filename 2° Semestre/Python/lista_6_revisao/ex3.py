def Contapalavras (frase):
    cont = 1
    for i in frase:
        if i == " ":
            cont +=1
    print(f'O total de palavras é: {cont}')

frase = input('Digite uma frase: ')

 

Contapalavras(frase)