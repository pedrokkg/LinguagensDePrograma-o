lista = []
tam = int(input("Qual será o tamanho da lista? "))


for i in range(tam):
    valor = int(input(f"Insira o {i+1}º valor: "))
    lista.append(valor)

maior=max(lista)
menor=min(lista)

print(f"O maior número da lista é: {maior}")
print(f"O menor número da lista é: {menor}")