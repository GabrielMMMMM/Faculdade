import time

i = 0
g = 0
w = 0
j = 0
print ("="*15)
print (" "*3, "Eleições")
print ("="*15)
print ("Canditatos: \nGabriel vote (1) \nJoão vote (2) \nWillian vote (3)")
print (" ")
eleitores = int (input("Digite o número total de eleitores: "))
while eleitores != 0 :
    i +=1
    votos =  int( input ("Eleitor N°"+ str(i)+" vote: "))
    print (" ")
    while votos >3 :
        print (" ")
        print ("Canditatos: \nGabriel vote 1 \nJoão vote 2 \nWillian vote 3")
        votos =  int (input("Eleitor N°"+ str(i)+" vote: "))
        print (" ")
    if votos == 1 :
        g +=1
    elif votos == 2:
        j +=1
    elif votos == 3:
        w +=1
    eleitores -= 1    
    
print ("Computando votos...")
time.sleep(3)
print (" ")
print (f"RESULTADO: \nGabriel: {g} votos. \nJoão: {j} votos. \nWillian: {w} votos.")  
if g > j and g >w :
    print("Gabriel foi eleito com a maioria dos votos!")
elif j > g and j > w:
    print("João foi eleito com a maioria dos votos!")              
elif w > g  and w >j:
    print ("Willian foi eleito com a maioria dos votos!")
else:
    print ("As Eleições empataram!")
