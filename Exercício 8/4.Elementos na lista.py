def acessar_indice():
    lista = [10, 20, 30, 40, 50]
    try:
        indice = int(input("Digite um índice (0 a 4) para acessar um valor da lista: "))

        valor = lista[indice]
        
        print(f"O valor no índice {indice} é {valor}.")
    
    except IndexError:
        print("Erro: Índice inválido. O índice deve estar entre 0 e 4.")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido para o índice.")

acessar_indice()
