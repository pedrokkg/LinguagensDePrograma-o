classificao=("Fluminense","Grêmio", "Palmeiras", "Flamengo", "Corinthians","Internacional","Bahia","Santos","São Paulo","Figueirense")

#Primeiros 3
print(classificao[:3])

#Os últimos três colocados.
print(classificao[-3:])

#Alfabética
print("\nTimes em ordem alfabética:")
print(sorted(classificao))

#Time específico
time_especifico = input("\nDigite o nome de um time para saber sua posição no campeonato: ")

if time_especifico in classificao:
    print(f"\nO time {time_especifico} está na posição {classificao.index(time_especifico) + 1}.")
else:
    print("\nTime não encontrado na lista.")
