print ("="*15)
print ("LOJA QUASE DOIS")
print ("="*15)
c = 1
i = 1
while  i <= 50:
    print (str (c)+ " - ", 1.99*c )
    c +=1
    i +=1


produtos = int (input("Quantos produtos o cliente comprou: "))
total = produtos *1.99
print(f"O valor total da compra é de {total} reais.")