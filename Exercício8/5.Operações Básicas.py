def realizar_saque():
    saldo = 1000
    try:
        saque = float(input("Digite o valor para saque: R$ "))
        
        if saque > saldo:
            raise ValueError(f"Erro: Saldo insuficiente. Tentativa de saque: R${saque}, Saldo disponível: R${saldo}")
        
        saldo -= saque
        print(f"Saque realizado com sucesso. Saldo restante: R$ {saldo:.2f}")
    
    except ValueError as e:
        print(e)
        
realizar_saque()