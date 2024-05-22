n = float(input("Digite um número: "))
b = 2.0
epsilon = 0.001

while abs(n - b * b) > epsilon:
    p = (b + (n / b)) / 2.0
    b = p

print(f'A raíz quadrada é aproximadamente {b:.3f}')
