def remove_lista(nu):
    x.pop(nu)
    print(x)
x = []
for i in range (5):
    n = int (input("Digite um número para add na lista: "))
    x.append(n)
print (x)    
nu = int (input("Digite um número para remover da lista: "))    
remove_lista(nu)