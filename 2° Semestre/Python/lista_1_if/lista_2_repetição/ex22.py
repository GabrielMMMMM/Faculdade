
while True:

    t = str(input('Digite o tipo da taboada (SOMA/SUBTRAÇÃO/DIVISÃO/MULTIPLICAÇÃO) ou (SAIR): ')).lower()

    if t == "sair":
        break
    
    n = int(input('Digite o valor do número: '))

    match t:
        case "soma":
            for i in range (1, 11):
                print(f'{n} + {i} = {n+i}')
        case "subtração":
            for i in range (1, 11):
                print(f'{n} - {i} = {n-i}')    
        case "multiplicação":
            for i in range (1, 11):
                print(f'{n} * {i} = {n*i:.2f}')    
        case "divisão":
            for i in range (1, 11):
                print(f'{n} / {i} = {n/i:.2f}')         
        case _:
            print("Operação Invalida!")   
                    