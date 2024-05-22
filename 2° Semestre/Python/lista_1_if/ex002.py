multa = 0
vel =int(input("Digite em km/h a velocidade que seu carro estava correndo: "))
if vel > 80:
    multa = (vel-80)*5
    print (f"Como você ultrapassou o limite de velocidade, então você tem que pagar uma multa de {multa} reais.")
else:
    print("Você respeitou o limite de velocidade, não será mudado pode continuar o seu caminho.")
