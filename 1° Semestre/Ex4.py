a = int (input("Digite a quantas pessoas tem no país A: "))
taxa = float(input("Digite a taxa de crecimento da população A: "))

b = int (input("Digite a quantas pessoas tem no país B: "))
taxb = float(input("Digite a taxa de crecimento da população B: "))
anos = 0
while a < b :
    b *=taxb * 1
    a *= taxa * 1 
    anos += 1

print(f"A população 'a' precisa de {anos} anos para alcanar a população 'b'.")