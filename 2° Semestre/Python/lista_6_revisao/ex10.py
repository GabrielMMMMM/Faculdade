import random

numero_secreto = random.randint(1, 100)

tentativas = 0
max_tentativas = 10

print("Bem-vindo ao Jogo de Adivinhação!")
print(f"Tente adivinhar um número entre 1 e 100. Você tem {max_tentativas} tentativas.")

while tentativas < max_tentativas:
    try:
        palpite = int(input("Digite o seu palpite: "))

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas + 1} tentativa(s).")
            break
        elif palpite < numero_secreto:
            print(f"O número secreto é maior. Tente novamente. Você tem mais {9 - tentativas} tentativas.")
        else:
            print(f"O número secreto é menor. Tente novamente. {9 - tentativas}. tentativas.")

        tentativas += 1
    except ValueError:
        print("Por favor, digite um número válido.")

if tentativas == max_tentativas:
    print(f"Suas {max_tentativas} tentativas acabaram. O número secreto era {numero_secreto}.")
