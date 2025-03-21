numeros = (
    int(input("Digite o primeiro número: ")),
    int(input("Digite o segundo número: ")),
    int(input("Digite o terceiro número: ")),
    int(input("Digite o quarto número: "))
)

print(f"O número 9 apareceu {numeros.count(9)} vez(es).")

if 3 in numeros:
    print(f"O primeiro número 3 foi digitado na posição {numeros.index(3) + 1}.")
else:
    print("O número 3 não foi digitado.")

pares = [num for num in numeros if num % 2 == 0]
print(f"Números pares na tupla: {pares}")