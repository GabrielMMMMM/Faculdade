def media():
    a = sum(x)
    b = len(x)
    print(f'A média dos valores digitados é {a/b}')
x = []
i = 1
while i < 6:
    c = int (input(f"Digite o {i}° para fazer a média: "))
    i+=1
    x.append(c)    
media()