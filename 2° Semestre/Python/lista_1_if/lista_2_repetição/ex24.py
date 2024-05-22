valor = int(input('Digite um número: '))

print('\n' + 'Números Primos:')

for x in range(2, valor + 1, 1):
  if x == 2:
    print(x)
  else:
    primo = True
    
    if x % 2 == 0:
      primo = False
    else:
      for i in range(3, x, 2):
        if x != i and x % i == 0:
            primo = False

    if primo:
     print(x)