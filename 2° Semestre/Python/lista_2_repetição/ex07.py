n = int(input("Digite um número: "))
n1= int(input("Digite o começo da tabuada: "))
n2= int(input("Digite o fim da tabuada: "))
while n2<n1:
   print("Digite um número maior que o anterior!")
   n2= int(input("Digite o fim da tabuada: "))

while n1 <= n2:
   print(f"{n} * {n1} = {n*n1}")
   n1+=1