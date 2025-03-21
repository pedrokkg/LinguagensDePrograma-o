tam = int(input("Quantos produtos serão inseridos? "))
i = 0

while i < tam:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))
    quantidade = int(input("Digite a quantidade em estoque: "))
    
    produto = (nome, preco, quantidade)
    
    print("\nInformações do Produto:")
    print(f"Nome do produto: {produto[0]}")
    print(f"Preço: R${produto[1]:.2f}")
    print(f"Quantidade em estoque: {produto[2]}")
    print("\n")
    
    print(produto)
    i += 1
