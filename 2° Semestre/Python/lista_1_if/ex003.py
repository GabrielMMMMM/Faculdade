print ("Digite 3 números e mostraremos o MAIOR e o MENOR.")
n1 = int(input("Digite o 1° número:"))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 3° número: "))

if n1 == n2 and n2 == n3 :
    print("Todos os números são iguais!")
elif n1 > n2 and n2 >n3:
    print (f"O maior número é {n1} e o menor é o {n3}")
elif n1 > n2 and n3 >n2:
    print(f"O maior número é {n1} e o menor é o {n2}")
elif n2 > n1 and n1 >n3:
    print(f"O maior número é {n2} e o menor é o {n3}")
elif n2 > n1 and n3 >n1:
    print(f"O maior número é {n2} e o menor é o {n1}")
elif n3 > n1 and n1 >n2:
    print(f"O maior número é {n3} e o menor é o {n2}")
elif n3 > n2 and n2 > n1:
    print(f"O maior número é {n3} e o menor é o {n1}") 
