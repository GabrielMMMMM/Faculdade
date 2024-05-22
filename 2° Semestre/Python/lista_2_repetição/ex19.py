import time 

dinheiro = float(input('Digite o valor a ser sacado: '))
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0

while dinheiro > 0:

    if dinheiro >= 100:
        dinheiro -= 100
        f +=1
    elif dinheiro >= 50:
        dinheiro -= 50
        a +=1
    elif dinheiro >= 20:
        dinheiro -= 20
        b +=1    
    elif dinheiro >= 10:
        dinheiro -= 10
        c +=1    
    elif dinheiro >= 4:
        dinheiro -= 4
        d +=1    
    elif dinheiro >=1:
        dinheiro -= 1
        e +=1 
    elif dinheiro >=0.5:
        dinheiro -= 0.5
        g +=1 
    elif dinheiro >=0.1:
        dinheiro -= 0.1
        h +=1 
    elif dinheiro >=0.05:
        dinheiro -= 0.05
        i +=1 
    elif dinheiro >=0.02:
        dinheiro -= 0.02
        j +=1 
    elif dinheiro >=0.01:
        dinheiro -= 0.01
        k +=1                     
   


print('Imprimindo...')

time.sleep(5)  
print ("="*15)  
print ('NOTAS SACADAS')
print ("="*15)     

print(f'Notas de 100 reais:{f}.')
print(f'Notas de 50 reais: {a}.')
print(f'Notas de 20 reais: {b}.')
print(f'Notas de 10 reais: {c}.')
print(f'Notas de  4 reais: {d}.')
print(f'Notas de   1 real: {e}.')
print(f'Moedas de 50 centavos: {g}.')
print(f'Moedas de 10 centavos: {h}.')
print(f'Moedas de 5 centavos:  {i}.')
print(f'Moedas de 2 centavos:  {j}.')
print(f'Moedas de 1 centavo:   {k}.')
