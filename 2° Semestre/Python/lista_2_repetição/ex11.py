deposito = float(input('Digite o quando você deseja depositar: R$'))
juros = float(input("Digite quando de juros renderá por mês em %: "))
a = deposito

for i in range(24):
    deposito += deposito*(juros/100)
    print(f'No {i+1}° mês você ganhou: R${deposito:,.2f}')
  
print (f'Total de juros ganho: R${deposito-a:,.2f}')  