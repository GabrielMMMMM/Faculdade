def conta_vogais(palavra):
    cont = 0
    vogais = "aeiou"
    for i in palavra:
        if i in vogais:
            cont +=1
    print(f"O número de voigais é {cont}")        

palavra = str (input("Digite uma palavra: ")).lower()

conta_vogais(palavra)