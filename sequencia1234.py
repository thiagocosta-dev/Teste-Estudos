def sequencia(n):
    for c in range(1, n + 1):
        for j in range(1, c + 1):
            print(j, end="")
        print()


sequencia(12)
