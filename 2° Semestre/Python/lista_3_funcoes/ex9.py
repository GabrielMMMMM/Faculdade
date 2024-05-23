def soma_intervalo():
    a = 0
    if nu > n:
        for i in range (n+1, nu):
            a += i
    else: 
        for i in range (nu+1, n):
            a += i        
    print(f"A soma dos valores entre {nu} e {n} é {a}")        

nu = int(input("Digite um número: "))
n = int(input("Digite outro número: "))
soma_intervalo()    