deposito = float(input('Digite o quando você deseja depositar: R$'))
juros = float(input("Digite quando de juros renderá por mês em %: "))
a = deposito
meses = 0

for i in range(3):
    deposito += deposito*(juros/100)
    print(f'No {i+1}° mês você ganhou: R${deposito:,.2f}')
    b = str(input('Deseja depositar mais dinhero? (S/N): ')).lower()
    if b == "s":
        mes = float(input('Digite o valor do depósito: R$'))
        deposito += mes
        meses+=mes
  
print (f'Total de juros ganho: R${(deposito-meses)-a:,.2f}')  