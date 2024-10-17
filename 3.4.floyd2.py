def floyd2(n, W):
    P = [[-1] * (n) for _ in range(n)]
    D = W
    # Complete the code here
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    P[i][j] = k
                    D[i][j] = D[i][k] + D[k][j]

    return D, P


def path(i, j):
    k = P[i][j]
    if k != -1:
        path(i, k)
        print("v" + str(k), end=" ")
        path(k, j)


INF = float("inf")

# Example 1
print("######Example 1######")
n = 5
W = [
    [0, 1, INF, 1, 5],  # v0 -> vi
    [9, 0, 3, 2, INF],  # v1 -> vi
    [INF, INF, 0, 4, INF],  # v2 -> vi
    [INF, INF, 2, 0, 3],  # v3 -> vi
    [3, INF, INF, INF, 0],
]  # v4 -> vi

D, P = floyd2(n, W)
print("D = ")
for i in range(n):
    print(D[i])
print("P = ")
for i in range(n):
    print(P[i])

path(4, 2)

# # Example 2 - Your Custom Case
print("######Example 2 #######")
# # Insert your example here
n = 5
W = [
    [0, INF, 4, INF, INF],
    [1, 0, INF, 1, INF],
    [INF, 2, 0, 6, INF],
    [3, INF, INF, 0, 2],
    [INF, INF, INF, INF, 0],
]

# raise NotImplementedError("Complete your example.")
D, P = floyd2(n, W)
print("D = ")
for i in range(n):
    print(D[i])
print("P = ")
for i in range(n):
    print(P[i])

path(3, 2)
