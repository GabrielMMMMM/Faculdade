def trocar(a, b):
    temp = a
    a = b
    b = temp
    return a, b


valor1 = 5
valor2 = 10
print("Antes da troca:")
print("Valor 1:", valor1)
print("Valor 2:", valor2)

valor1, valor2 = trocar(valor1, valor2)

print("Após a troca:")
print("Valor 1:", valor1)
print("Valor 2:", valor2)

