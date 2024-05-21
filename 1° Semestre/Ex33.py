N = int(input("Digite a quantidade de termos da série: "))

soma = 0.0

for i in range(1, N + 1):
    termo = 1 / i
    soma += termo

print("Valor de H com", N, "termos:", soma)
