dicionario={
    'game':'jogo',
    'play':'jogar',
    'watch':'assistir'
}

palavra = input("Digite uma palavra em português para traduzir: ").lower()

if palavra in dicionario:
    print(f"A tradução de '{palavra}' é '{dicionario[palavra]}'.")
else:
    print("Desculpe, a tradução não foi encontrada.")