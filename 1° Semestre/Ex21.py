salario = float(input("Digite o salário: "))
reajuste = 0.015
ano = 1995
while ano <= 2023 :
    print (f"O reajuste salarial do ano de {ano} foi de {reajuste} e o salário foi de R$ {salario: .2f}")
    ano += 1
    salario *= reajuste
    reajuste *=2
   