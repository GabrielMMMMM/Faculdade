resultado =0 
c= 1
while c != 0:
    c = int(input('Digite o código do produto (1,2,4,5,9), digite 0 caso queria finalizar: '))
    match c:
        case 1:
            produtos = int(input('Quantos produtos você comprou? '))
            total = produtos * 0.50
        case 2:
            produtos = int(input('Quantos produtos você comprou? '))
            total = produtos * 1
        case 4:
            produtos = int(input('Quantos produtos você comprou? '))
            total = produtos * 4
        case 5:
            produtos = int(input('Quantos produtos você comprou? '))
            total = produtos * 7
        case 9:
            produtos = int(input('Quantos produtos você comprou? '))
            total = produtos * 8
        case _:
            print("Código Invalido!")       
    resultado += total

print(f'\nO total da sua compra foi de {resultado} reais.')    
        