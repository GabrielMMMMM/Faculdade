numero = int(input("Digite um número: "))
numero_str = str(numero)

if numero_str == numero_str[::-1]:
    print(f"{numero} é um número palíndromo.")
else:
    print(f"{numero} não é um número palíndromo.")
