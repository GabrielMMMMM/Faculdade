def calculaProduto(list):
    maiorproduto = 0
    for i in range (0, len(list)):
        for y in range(0,len(list)):
            if i != y:
                maior = list[i]*list[y]
                if maior > maiorproduto:
                    maiorproduto = maior
    print (maiorproduto)
list = [5,2,3,4,1,10]
calculaProduto(list)