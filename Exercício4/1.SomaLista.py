lista = []
tam = int(input("Qual será o tamanho da lista? "))


for i in range(tam):
    valor = int(input(f"Insira o {i+1}º valor: "))
    lista.append(valor)


soma = sum(lista)


print(f"Valor da soma da lista é: {soma}")