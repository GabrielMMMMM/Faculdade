numeros = input("Digite 5 números separados por espaço: ")
a, b, c, d, e = map(int, numeros.split())

if a > b and a > c and a > d and a > e:
    print(f"O maior número é o {a}.")
elif b > a and b > c and b > d and b > e:
    print(f"O maior número é o {b}.")
elif c > a and c > b and c > d and c > e:
    print(f"O maior número é o {c}.")
elif d > a and d > b and d > c and d > e:
    print(f"O maior número é o {d}.")
else:
    print(f"O maior número é o {e}.")
