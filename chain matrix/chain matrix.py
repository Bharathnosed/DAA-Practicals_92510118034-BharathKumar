def matrix_chain(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = 999999999

            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def order(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        order(s, i, s[i][j])
        order(s, s[i][j] + 1, j)
        print(")", end="")


p = list(map(int, input("Enter dimensions: ").split()))
m, s = matrix_chain(p)

print("Minimum multiplications:", m[1][len(p) - 1])
print("Optimal matrix order: ", end="")
order(s, 1, len(p) - 1)
print()
