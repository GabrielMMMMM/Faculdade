valor_divida = float(input("Digite o valor da dívida: "))
taxa_juros = float(input("Digite a taxa de juros (em %): "))
num_parcelas = int(input("Digite a quantidade de parcelas: "))

taxa_juros = taxa_juros / 100  

valor_juros = valor_divida * taxa_juros
valor_total = valor_divida + valor_juros
valor_parcela = valor_total / num_parcelas

print("\nTabela de Pagamento:")
print("========================================")
print(f"Valor da Dívida: R$ {valor_divida:.2f}")
print(f"Valor dos Juros: R$ {valor_juros:.2f}")
print(f"Quantidade de Parcelas: {num_parcelas}")
print(f"Valor da Parcela: R$ {valor_parcela:.2f}")
print("========================================")
