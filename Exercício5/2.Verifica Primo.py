
def verificar_e_imprimir_primo(n):
    if n <= 1:
        print(f"O número {n} não é primo.")
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            print(f"O número {n} não é primo.")
            return False
    print(f"O número {n} é primo.")  
    return True

numero = int(input("Digite um número inteiro para verificar se é primo: "))

verificar_e_imprimir_primo(numero)