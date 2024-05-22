divida = float(input('Digite o valor da divida: R$'))
juro = float(input('Digite o valor do juros em %: '))
mes = float(input('Digite o valor mensal que será pago: R$'))
i = 0
total = divida
juross=0

while divida > 0:
    juros = divida*(juro/100)
    divida += juros
    divida -= mes
    juross+=juros
    i +=1
    if divida <0:
        divida =0

print(f'\nA dívida será paga em: {i} meses.')
print(f'O total pago foi de: R${total+juross:,.2f}.')
print(F'O valor do juros foi de: R${juross:,.2f}.')