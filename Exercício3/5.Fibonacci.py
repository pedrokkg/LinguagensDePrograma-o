N = int(input("Digite o número de termos da sequência de Fibonacci: "))
a = 0
b = 1
for _ in range(N):
    print(a, end=' ')
    a = b
    b = a + b