def calculaFribonacci(n):
    lista = [0, 1]
    cont = 0
    x = 0
    y = 1
    while cont != n - 2:
        f = x+y
        x = y
        y = f
        lista.append(f)
        cont += 1
    return lista


print(calculaFribonacci(n=int(input("Digite um número: "))))
