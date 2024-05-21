def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

N = int(input("Digite um número: "))

numeros_primos = []
divisoes = 0

for i in range(2, N + 1):
    if verificar_primo(i):
        numeros_primos.append(i)
    divisoes += 1

print("Números primos encontrados:")
for primo in numeros_primos:
    print(primo)

print(f"\nTotal de divisões realizadas: {divisoes}")
