import time 

dinheiro = int(input('Digite o valor a ser sacado: '))
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
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
