def fatorial():
    a = 1
    for i in range (nu, 1, -1):
        a *= i
    print(f'O fatorial de {nu} é {a}')

nu = int(input('Digite um número: '))  

fatorial()