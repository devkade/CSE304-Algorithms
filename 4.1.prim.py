def prim(n, W):
    F = []
    vnear = 0
    for i in range(2, n + 1):
        nearest[i] = 1
        distance[i] = W[1][i]
    for _ in range(n - 1):
        # Complete the code here
        minVal = INF
        for i in range(2, n + 1):
            if 0 <= distance[i] < minVal:
                minVal = distance[i]
                vnear = i

        edge = (nearest[vnear], vnear, W[nearest[vnear]][vnear])
        F.append(edge)
        distance[vnear] = -1

        for i in range(2, n + 1):
            if W[i][vnear] < distance[i]:
                distance[i] = W[i][vnear]
                nearest[i] = vnear

    return F


INF = float("inf")

# Example 1
print("######Example 1######")
n = 5  # the number of vertices
W = [  # adjacency matrix
    [INF, INF, INF, INF, INF, INF],
    [INF, 0, 1, 3, INF, INF],
    [INF, 1, 0, 3, 6, INF],
    [INF, 3, 3, 0, 4, 2],
    [INF, INF, 6, 4, 0, 5],
    [INF, INF, INF, 2, 5, 0],
]
nearest = [-1] * (n + 1)
distance = [-1] * (n + 1)

F = prim(n, W)
print(F)

# # Example 2 - Your Custom Case
print("######Example 2 #######")
# # Insert your example here
n = 5
W = [  # adjacency matrix
    [INF, INF, INF, INF, INF, INF],
    [INF, 0, 3, 1, 4, INF],
    [INF, 3, 0, 7, 3, INF],
    [INF, 1, 7, 0, 4, 2],
    [INF, 4, 3, 4, 0, 5],
    [INF, INF, INF, 2, 5, 0],
]
nearest = [-1] * (n + 1)
distance = [-1] * (n + 1)
# raise NotImplementedError("Complete your example.")
F = prim(n, W)
print(F)
