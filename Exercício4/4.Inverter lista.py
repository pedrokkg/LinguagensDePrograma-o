lista = []
tam = int(input("Qual será o tamanho da lista? "))


for i in range(tam):
    valor = input(f"Insira a {i+1}º palavra: ")
    lista.append(valor)

invertidas=lista[::-1]

print("Lista na ordem inversa:", invertidas)