agenda_telefonica = {}

print("A agenda telefônica está vazia.")

while True:
    nome = input("Digite o nome do contato (ou 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        break
    
    numero = input("Digite o número de telefone: ")
    
    agenda_telefonica[nome] = numero
    print("Contato adicionado com sucesso!")

print("\nContatos na agenda telefônica:")

for contato, numero in agenda_telefonica.items():
    print(f"- {contato}: {numero}")
