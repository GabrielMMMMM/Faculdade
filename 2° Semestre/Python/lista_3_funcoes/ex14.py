def area_retangulo(altura, largura):
    return altura*largura
    
h= int (input("Digite a altura do retângulo: "))
b = int (input('Digite a base do retângulo: '))
area = int(area_retangulo(b, h))
print(area)