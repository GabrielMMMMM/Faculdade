distancia = float(input("Digite quantos KM você quer percorrer: "))
if distancia <= 200:
    km = 0.50
    valor = distancia*km
    print(f"Você vai pagar 0,50 centavos por KM. O total da sua viagem deu {valor}")
else:
    km =0.45    
    valor = distancia*km
    print(f"Você vai pagar 0,45 centavos por KM. O total da sua viagem deu {valor}")
