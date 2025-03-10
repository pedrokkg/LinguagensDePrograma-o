lista = []
tam = int(input("Qual será o tamanho da lista? "))


for i in range(tam):
    valor = int(input(f"Insera o {i+1}º valor: "))
    lista.append(valor)

especifico=int(input("Insera o número específico"))

conta=lista.count(especifico)
print(f"O número {especifico} aparece {conta} vezes na lista.")