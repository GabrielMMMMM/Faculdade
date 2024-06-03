def calculoMDC(x, y):
    mdc = 1
    i = 2
    while x > 1 and y > 1:
        while x % i == 0 or y % i == 0:
            if x % i == 0 and y % i == 0:
                mdc *= i
            if x % i == 0:
                x /= i
            if y % i == 0:
                y /= i
        i += 1
    return mdc


numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

mdc_resultado = calculoMDC(numero1, numero2)
print(f"O MDC é {mdc_resultado}")
