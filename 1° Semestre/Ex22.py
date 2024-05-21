
mais_alto = 0
mais_baixo = 0
altura_alto = 0
altura_baixo = 0


for i in range(1, 11):
   
    numero = int(input(f"Digite o número do {i}º aluno: "))
    altura = float(input(f"Digite a altura do {i}º aluno em cm: "))

   
    if altura > altura_alto:
        altura_alto = altura
        mais_alto = numero
    if altura < altura_baixo or i == 1:
        altura_baixo = altura
        mais_baixo = numero


print(f"O aluno mais alto é o número {mais_alto} com {altura_alto} cm.")
print(f"O aluno mais baixo é o número {mais_baixo} com {altura_baixo} cm.")
