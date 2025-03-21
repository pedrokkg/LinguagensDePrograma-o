alunos=[]

for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota))
    
print("\nNomes dos alunos:")
for aluno in alunos:
    print(aluno[0])

print("\nNotas dos alunos:")
for aluno in alunos:
    print(aluno[1])