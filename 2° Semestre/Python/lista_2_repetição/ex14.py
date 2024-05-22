a=1
i = 0
media =0 
while a !=0 :
    a = int (input('Digite um número, caso queira parar digite 0: '))
    i += 1
    media += a
print(f'Total de números digitados: {i}. \nSoma dos números digitados: {media}. \nMédia dos números digitados: {media/i}' )    
