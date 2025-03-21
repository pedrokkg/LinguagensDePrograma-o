alunos = {}

while len(alunos) < 3:
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
 
    alunos[nome] = nota

print("\nLista de alunos e suas respectivas notas:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota:.1f}")