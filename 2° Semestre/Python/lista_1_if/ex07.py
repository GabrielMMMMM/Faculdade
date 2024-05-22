categoria = int(input("Digite a categoria do produto (1 a 5): "))

if categoria == 1:
    preco = 10.00
elif categoria == 2:
    preco = 15.00
elif categoria == 3:
    preco = 19.00
elif categoria == 4:
    preco = 23.00
elif categoria == 5:
    preco = 27.00
else:
    print("Categoria inválida")
    preco = 0.00

if preco > 0:
    print(f"O preço do produto na categoria {categoria} é de R$ {preco:.2f}")
