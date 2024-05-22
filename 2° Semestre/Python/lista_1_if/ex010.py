kwh_consumidos = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R para residencial, I para industrial, C para comércio): ")

if tipo_instalacao == "R" or tipo_instalacao == "r":
    if kwh_consumidos <= 500:
        preco_pagar = kwh_consumidos * 0.40
    else:
        preco_pagar = kwh_consumidos * 0.65
elif tipo_instalacao == "C" or tipo_instalacao == "c":
    if kwh_consumidos <= 1000:
        preco_pagar = kwh_consumidos * 0.55
    else:
        preco_pagar = kwh_consumidos * 0.60
elif tipo_instalacao == "I" or tipo_instalacao == "i":
    if kwh_consumidos <= 5000:
        preco_pagar = kwh_consumidos * 0.55
    else:
        preco_pagar = kwh_consumidos * 0.60
else:
    print("Tipo de instalação inválido")
    preco_pagar = 0.00

print(f"O preço a pagar pelo fornecimento de energia elétrica é de R$ {preco_pagar:.2f}")
