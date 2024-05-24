def lista_ordenada(x):
    a = sorted(x)
    print (a)

x= []
while True:
    n = int (input("Digite um número, digite 0 para sair: "))
    x.append(n)
    if n == 0:
        break
    
lista_ordenada(x)    