def mesma_quantidade():
    a = len (x)
    b = len (y)
    if a == b :
        print(f"Ambas as lista {a} números.")
    else:
        print(f"A primeira lista tem {a} números e a segunda tem {b} números.")
x = [] 
y = []
r = 0
re = 0
while r != "n":
    nu = (input("Digite um número para a primeira lista: "))
    x.append(nu)
    r = str(input("Deseja digitar mais um número? (S/N): ")).lower()
while re != "n":
    n =  (input("Digite um número para a segunda lista: "))
    y.append(n)
    re = str(input("Deseja digitar mais um número? (S/N): ")).lower()

mesma_quantidade()    
