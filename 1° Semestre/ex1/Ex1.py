import time 
nome = (input("Digite seu nome: "))
senha = (input("Crie uma senha: "))
while senha == nome :
    senha =  (input("Crie uma senha que não seja seu nome: "))
print ("Processando...")
time.sleep(5)    
print(f"Seu login : {nome} \nSua Senha: {senha}")