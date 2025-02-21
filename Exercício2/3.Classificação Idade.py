idade=int(input("Insira a sua idade: "))

if idade<18:
    classe="Menor de idade"
elif idade>19 and idade<=59:
    classe="Adulto"
elif idade>59:
    classe="Idoso"
    
print(f"Sua classe é: {classe}")
