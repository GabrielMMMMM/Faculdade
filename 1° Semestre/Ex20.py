mais_alto = 0
mais_baixo = 0
altura_alto = 0
altura_baixo = 0
i = 0
codigo = 1

while codigo != 0:
    codigo = int(input("Digite seu código ou digite 0 para encerrar o programa: "))
    if codigo == 0:
        break
    
    altura = int(input("Digite sua altura, em CM: "))
    peso = float(input("Digite seu peso em KG: "))
    
    if altura > altura_alto or i == 0:
        altura_alto = altura
        mais_alto = codigo
    if altura < altura_baixo or i == 0:
        altura_baixo = altura
        mais_baixo = codigo
        
    i += 1

print(f"O aluno mais alto é o número {mais_alto} com {altura_alto} cm.")
print(f"O aluno mais baixo é o número {mais_baixo} com {altura_baixo} cm.")
