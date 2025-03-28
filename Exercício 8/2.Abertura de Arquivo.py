def ler_arquivo():
    try:
        nome_arquivo = input("Digite o nome do arquivo para leitura: ")
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except IOError:
        print("Erro: Ocorreu um erro ao tentar ler o arquivo.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        
ler_arquivo()