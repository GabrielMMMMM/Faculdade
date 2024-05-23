def e_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    if palavra == palavra[::-1]:
        print(f"{palavra} é uma palavra palíndromo.")
    else:
        print(f"{palavra} não é um palavra palíndromo.")

palavra = str(input("Digite uma palavra: "))    
e_palindromo(palavra)

