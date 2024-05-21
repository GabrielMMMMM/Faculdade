nome = input("Digite seu nome: ")
while len(nome) <= 3: 
    print("Seu nome precisa ter mais que 3 caracteres!")
    nome = input("Digite seu nome: ")

idade = int (input("Digite sua idade: "))
while idade < 0 or idade > 150:
    if idade < 0:
        print ("Você não está vivo!")
        idade = int (input("Agora, digite sua idade: "))
    elif idade > 150: 
        print (f"Caramba quero chegar aos {idade} também!")    
        idade = int (input("Agora, digite sua idade: "))

salario = float (input("Digite seu salário: ")) 
while salario == 0 :
    print ("Você está pobre em...") 
    salario = float (input("Digite seu salário: "))

sexo = str (input("Digite seu sexo, 'M' para masculino, 'F' para feminino: ")).lower()
while sexo != "m" and sexo != "f":
  print("Caracter inválido!")
  sexo = str (input("Digite seu sexo, M para masculino, F para feminino: ")).lower()     
if sexo == "m":
    sexo = "Masculino"
else:
    sexo = "Feminino"  

ec = str (input("Digite seu estado civil, 'S' para solteiro, 'C' para casado: ")).lower()
while ec != "s" and ec != "c":
   print("Caracter inválido!")
   ec = str (input("Digite seu estado civil, 'S' para solteiro, 'C' para casado: ")).lower()
if ec == "s":
    ec = "Solteiro"
else:
    ex = "Casado"    
print("========================")
print("       SEUS DADOS        ")
print("========================")

print(f"Nome: {nome} \nIdade: {idade} \nSalário: {salario} \nSexo: {sexo} \nEstado Civil: {ec}")