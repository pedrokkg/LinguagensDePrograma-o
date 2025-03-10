lista = []
tam = int(input("Qual será o tamanho da lista? "))


for i in range(tam):
    valor = int(input(f"Insira o {i+1}º valor: "))
    lista.append(valor)

unicos=[]
for num in lista:
    if num not in unicos:
        unicos.append(num)

print("Lista sem duplicatas:", unicos)