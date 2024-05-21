N = int(input("Digite a quantidade de termos da série: "))

soma = 0.0
m = 1

for n in range(1, N + 1):
    termo = n / m
    soma += termo
    print(f"{n}/{m} = {termo}")
    m += 2

print("Soma da série:", soma)
