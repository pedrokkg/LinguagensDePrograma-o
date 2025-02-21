l1=float(input("Insira o Lado 1: "))
l2=float(input("Insira o Lado 2: "))
l3=float(input("Insira o Lado 3: "))

if (l1+l2)<l3:
    print("O triângulo não pode existir!")
elif l1+l3<l2:
    print("O triângulo não pode existir!")
elif l2+l3<l1:
    print("O triângulo não pode existir!")
else:
    print("Esse triângulo está válido!")
