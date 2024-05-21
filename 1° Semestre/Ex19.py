print ("="*13)
print ("LOJA TABAJARA")
print ("="*13)
c = 1
i = 1
total = 0
produto = 1 
print ("Digite os valores dos produtos abaixo, para finalizar digite '0' ")
while  produto != 0:
    produto = float(input("Digite o valor do " +str (c)+ "° Produto: "))
    c +=1
    total +=produto
print(f"O valor total da compra é de {total} reais.")
din = float (input("Insira seu dinheiro: "))
while din < total :
    print(f"Você ainda precisa pagar {total - din} reais.")
    din = float (input("Insira seu dinheiro: "))
    din += din
troco = din - total
print (f"Seu troco é de {troco} reais.")     
print ("Obrigado pela preferência!")