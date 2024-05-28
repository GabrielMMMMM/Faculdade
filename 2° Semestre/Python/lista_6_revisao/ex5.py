def verificaPalindromo(palavra):
    if palavra == palavra[::-1] :
        return 1
    else:
        return 0 
palavra = str (input("Digite uma palavra: ")).lower()

 

print(f'{verificaPalindromo(palavra)}')