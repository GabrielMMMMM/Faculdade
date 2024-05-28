def contaCarecteresUnicos (palavra):
    cont = 0
    totaldeletras = len(palavra)
    for i in palavra:
        for y in palavra:
            if i == y:
                cont+=1
            
    letrasrepitidas =  cont - totaldeletras

    if letrasrepitidas == 0:
        print("Todas as letras são diferentes.")
    else:    
        letrasUnicas =  totaldeletras- letrasrepitidas
        print (f"O total de letras não repitidas é {letrasUnicas}.")    

palavra = input("Digite uma palavra: ").lower()

contaCarecteresUnicos(palavra)
