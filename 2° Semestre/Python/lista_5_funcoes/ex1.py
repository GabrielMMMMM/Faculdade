def verificaPrimo(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n <= 1 :
        return False 
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

n = int (input("Digite um número: "))

if verificaPrimo(n):
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")    
