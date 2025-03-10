
def calcular_media(lista):
    if len(lista) == 0:
        return 0  
    return sum(lista) / len(lista)


lista = []
tam = int(input("Qual será o tamanho da lista? "))


for i in range(tam):
    valor = int(input(f"Insira o {i+1}º valor: "))
    lista.append(valor)


media = calcular_media(lista)
print(f"A média dos números é: {media}")