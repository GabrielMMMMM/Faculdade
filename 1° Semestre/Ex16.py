cd = int (input("Diga uantos CD's você tem na sua coleção: "))
i = cd
valors = 0
c = 1
while i != 0:
    valor = float(input("Qual é o valor do "+ str(c)+ "° CD: "))
    i -= 1
    c += 1
    valors +=valor
media = valors /cd
print(f"O total investido foi de: {valors}. \nA média gasta foi de {media}.")

