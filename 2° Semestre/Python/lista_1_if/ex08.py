nu1 = float(input("Digite um número: "))
nu2 = float(input("Digite outro número: "))
oper = str(input("Digite a operação: "))


match (oper):
    case ("+"):
        print(f"{nu1} + {nu2} = {nu1+nu2}")
    case ("-"):
        print(f"{nu1} - {nu2} = {nu1-nu2}")
    case ("*"):
        print(f"{nu1} * {nu2} = {nu1*nu2}")
    case ("/"):
        if nu2 == 0:
            print("Não é possivel realizar essa divisão!")
        else:
            print(f"{nu1} / {nu2} = {nu1/nu2}")
