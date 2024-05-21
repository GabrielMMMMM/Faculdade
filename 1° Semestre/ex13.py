p = int (input("Digite quantas pessoas têm na sua sala: "))
idade=0
i =0 
while p != 0:
    i += 1
    idade1 = int (input ("Digite a idade da "+ str(i)+"° pessoa: "))
    idade += idade1
    p -=1
if p == 0:    
    media = 0
else:
    media = idade /i
if media <=20:
    print ("Turma é jovem")
elif  media <=60:
    print ("Turma Adulta") 
else:
    print("Turma Idosa")       