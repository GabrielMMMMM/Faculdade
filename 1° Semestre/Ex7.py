numero = input('Digite 5 anos separados por espaços: ')
a, b, c, d, e = map(int, numero.split())
media = (a+b+c+d+e)/5
print(f"A média dos números digitados é: {media}")