n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
i=0
t= n1
while n1 >= n2:
    n1-=n2
    i+=1

   
print(f'Resultado da divisão entre {t} e {n2} é: {i}')
print(f'O resto da divisão é: {n1}')