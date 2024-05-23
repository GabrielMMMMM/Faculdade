def contador_vogairs():
    cont = 0
    for i in palavra:
        if i == "a":
            cont += 1
        elif i == "e":
            cont += 1
        elif i == "i":
            cont += 1
        elif i == "o":
            cont += 1
        elif i == "u":
            cont += 1    
    print(f'O número de vogais é {cont}')    
palavra = str  (input('Digite uma palavra: '))
contador_vogairs()