def calcular_numeros_primos(numero):
    if numero < 2:
        return False, []

    divisores = []
    for i in range(2, int(numero/2) + 1):
        if numero % i == 0:
            divisores.append(i)

    if len(divisores) > 0:
        return False, divisores
    else:
        return True, []

numero = int(input("Digite um número: "))

primo, divisores = calcular_numeros_primos(numero)

if primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo. É divisível por: {divisores}")
