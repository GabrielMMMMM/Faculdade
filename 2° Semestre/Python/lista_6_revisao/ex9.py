def verificaPalindromo(frase):
    if frase == frase[::-1] :
        return 1
    else:
        return 0 
frase = str (input("Digite uma frase: ")).lower()

 

print(f'{verificaPalindromo(frase)}')