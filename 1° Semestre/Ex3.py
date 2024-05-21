a = 80000
b = 200000
anos = 0
while a < b :
    b *=1.015 * 1
    a *= 0.03 * 1 
    anos += 1

print(f"A população 'a' precisa de {anos} anos para alcanar a população 'b'.")
