# Dicionário com os itens do cardápio e seus preços
cardapio = {
    100: {"item": "Cachorro Quente", "preco": 1.20},
    101: {"item": "Bauru Simples", "preco": 1.30},
    102: {"item": "Bauru com ovo", "preco": 1.50},
    103: {"item": "Hambúrguer", "preco": 1.20},
    104: {"item": "Cheeseburguer", "preco": 1.30},
    105: {"item": "Refrigerante", "preco": 1.00}
}

total_pedido = 0

while True:
    codigo = int(input("Digite o código do item (ou -1 para encerrar o pedido): "))

    if codigo == -1:
        break

    quantidade = int(input("Digite a quantidade desejada: "))

    if codigo in cardapio:
        item = cardapio[codigo]
        preco_item = item["preco"]
        valor_item = preco_item * quantidade

        print(f"\nItem: {item['item']}")
        print(f"Preço unitário: R$ {preco_item:.2f}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor a ser pago: R$ {valor_item:.2f}")

        total_pedido += valor_item
    else:
        print("Código inválido. Tente novamente.")

print("\nTotal do pedido: R$", total_pedido)
