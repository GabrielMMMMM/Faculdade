contador_intervalos = [0, 0, 0, 0]  

while True:
    numero = int(input("Digite um número positivo (ou negativo para encerrar): "))

    if numero < 0:
        break 

    if 0 <= numero <= 25:
        contador_intervalos[0] += 1
    elif 26 <= numero <= 50:
        contador_intervalos[1] += 1
    elif 51 <= numero <= 75:
        contador_intervalos[2] += 1
    elif 76 <= numero <= 100:
        contador_intervalos[3] += 1

print("\nResultados:")
print("[0-25]:", contador_intervalos[0])
print("[26-50]:", contador_intervalos[1])
print("[51-75]:", contador_intervalos[2])
print("[76-100]:", contador_intervalos[3])
