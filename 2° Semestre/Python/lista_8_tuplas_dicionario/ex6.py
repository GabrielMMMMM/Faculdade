tupla = ()

for i in range(5):
    i += 1
    tupla += (i,)

adivinha = int(input("Digite um número para verificar se está na tupla: "))

encontrado = False
for elemento in tupla:
    if adivinha == elemento:
        encontrado = True
        break

if encontrado:
    print("Esse número está na tupla.")
else:
    print("Esse número não está na tupla.")
