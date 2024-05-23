def e_primo(n):
    if n%1 == 0 and n%n == 0 and n%2 != 0:
        print("É primo")
    elif n == 2: 
        print("É primo")   
    else:
        print("Não é primo")    

n = int(input('Digite um número: '))
e_primo(n)