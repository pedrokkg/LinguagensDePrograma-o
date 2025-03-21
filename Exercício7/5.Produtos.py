produtos = {
    101: ("Arroz", 20.50),
    102: ("Feijão", 15.30),
    103: ("Café", 10.99),
    104: ("Açúcar", 5.40),
    105: ("Macarrão", 8.99)
}

codigo = int(input("Digite o código do produto para buscar: "))

if codigo in produtos:
    nome, preco = produtos[codigo]
    print(f"\nProduto: {nome}")
    print(f"Preço: R${preco:.2f}")
else:
    print("\nCódigo de produto não encontrado.")
