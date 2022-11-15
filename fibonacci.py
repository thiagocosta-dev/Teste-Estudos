def fibonacci(num):
    t2 = 1
    t3 = 0
    soma = []
    for c in range(1, num + 1):
        print(f'{t3}', end=" ")
        soma.append(t3)
        t1 = t2
        t2 = t3
        t3 = t1 + t2
    resultado = sum(soma)
    print(f'\nResultado da soma: {resultado}')

fibonacci(5)
fibonacci(7)
