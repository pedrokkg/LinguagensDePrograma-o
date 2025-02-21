nota1=float(input("Insira sua nota 1: "))
nota2=float(input("Insira sua nota 2: "))
media=(nota1+nota2)/2

if media>=7:
    situacao="Aprovado"
elif media>5 and media<=6.9:
    situacao="Recuperação"
elif media<5:
    situacao="Reprovado"

print(f"Sua situação atual é: {situacao}")