def minimum(i, j, M, d):
    minvalue, mink = INF, 0
    for k in range(i, j):
        # Complete the code here
        if minvalue > M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]:
            minvalue = M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]
            mink = k

    return minvalue, mink


def minmult(n, d):
    M = [[INF] * (n + 1) for _ in range(n + 1)]
    P = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][i] = 0
    for diagonal in range(1, n):
        # Complete the code here
        # Tip. Implement minimum() and use it
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i][j], k = minimum(i, j, M, d)
            P[i][j] = k

    return M[1][n], M, P


def order(i, j, P):
    if i == j:
        return "A" + str(i)
    else:
        # Complete the code here
        k = P[i][j]
        return "(" + order(i, k, P) + order(k + 1, j, P) + ")"


INF = float("inf")

# Example 1
print("######Example 1######")
n = 6
d = [5, 2, 3, 4, 6, 7, 8]
minvalue, M, P = minmult(n, d)
print("M = ")
for i in range(1, n + 1):
    print(M[i][i:])
print("P = ")
for i in range(1, n + 1):
    print(P[i][i:])
print("minmult = ", minvalue)

multorder = order(1, n, P)
print(multorder)


# # Example 2 - Your Custom Case
print("######Example 2 #######")
# # Insert your example here
n = 4
d = [3, 2, 1, 5, 4]
# raise NotImplementedError("Complete your example.")
minvalue, M, P = minmult(n, d)
print("M = ")
for i in range(1, n + 1):
    print(M[i][i:])
print("P = ")
for i in range(1, n + 1):
    print(P[i][i:])
print("minmult = ", minvalue)

multorder = order(1, n, P)
print(multorder)

