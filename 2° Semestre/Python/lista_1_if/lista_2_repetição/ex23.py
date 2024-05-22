def prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

# Solicita o número ao usuário
numero = int(input("Digite um número inteiro positivo: "))

if prime(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
