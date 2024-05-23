def lista_ordenada():
    lista_crescente = sorted(x)      
    print (f"A lista em ordem crescente: {lista_crescente}")  

x = []
for i in range (5):
    n = int (input("Digite um número:"))
    x.append(n) 

lista_ordenada()    