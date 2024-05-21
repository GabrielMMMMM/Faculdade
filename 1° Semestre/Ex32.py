n = int(input("Digite a quantidade de termos da série: "))

soma = 0.0
m = 1

for i in range(1, n + 1):
    termo = i / m
    soma += termo
    print(f"{i}/{m} = {termo}")
    m += 2

print("Soma da série:", soma)
