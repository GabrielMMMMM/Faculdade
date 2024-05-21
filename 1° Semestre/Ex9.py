r = 0 
total = 0
while r != "n":
    fat = int (input ("Digite um número, inteiro positivo e menor que 16: "))
    while fat > 16 or fat < 0 :
        fat = int (input ("Digite um número, inteiro positivo e menor que 16: "))
    i = fat 
    total += 1
    while i != 1 :
        i -= 1
        fat *=  i
    print (f"O fatorial é {fat}")
    r = input ("Deseja fazer mais um calculo? (s/n) ").lower()
print (f"Você fez {total} contas.")

