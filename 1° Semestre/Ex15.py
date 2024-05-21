turma = int (input("Quantas turmas têm na escola: "))
i = turma
c= 1
alunos = 0
while i != 0 :
    aluno = int (input("Quantos alunos tem na " + str(c)+"° turma (Máx de 40 alunos por turma): "))
    while aluno > 40 :
        aluno = int (input("Quantos alunos tem na " + str(c)+"° turma (Máx de 40 alunos por turma): "))
    i -= 1
    alunos += aluno
    c+=1
media = alunos /turma 
print (f"A média de alunos em cada turma é de {media}")                