valor_casa = float(input("Digite o valor da casa a comprar: R$ "))
salario = float(input("Digite o seu salário mensal: R$ "))
anos_a_pagar = int(input("Digite a quantidade de anos a pagar: "))

meses_a_pagar = anos_a_pagar * 12
prestacao_mensal = valor_casa / meses_a_pagar
limite_prestacao = salario * 0.3

if prestacao_mensal <= limite_prestacao:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação mensal: R$ {prestacao_mensal:.2f}")
else:
    print("Empréstimo negado. Valor da prestação mensal excede 30% do salário.")
