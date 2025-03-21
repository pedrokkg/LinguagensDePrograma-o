fraseUser=input("Insira alguma frase: ").lower()
separados=fraseUser.split()

contagem={}

for palavra in separados:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
        
print("\nContagem de palavras na frase:")
print(contagem)