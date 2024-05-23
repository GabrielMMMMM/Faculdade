def inverte_lista():
    nova_lista= []
    a = len (x) -1
    while a >=0:
        nova_lista.append(x[a])
        a += -1
    print(f"Os números invertidos são: {nova_lista}")
x =[]
for i in range (6):
    b = int(input('Digite um número: '))
    x.append(b)
inverte_lista()    