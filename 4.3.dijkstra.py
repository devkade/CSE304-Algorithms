def dijkstra(n, W):
    F = []
    for i in range(2, n + 1):
        touch[i] = 1
        length[i] = W[1][i]
    for _ in range(n - 1):
        # Complete the code here
        minVal = INF
        # i vertex에서 가장 가까운 정점 뽑기
        for i in range(2, n + 1):
            if 0 <= length[i] < minVal:
                minVal = length[i]
                vnear = i

        edge = (touch[vnear], vnear, W[touch[vnear]][vnear])
        F.append(edge)
        length[vnear] = -1

        for i in range(2, n + 1):
            if length[vnear] + W[vnear][i] < length[i]:
                length[i] = length[vnear] + W[vnear][i]
                touch[i] = vnear

    return F


INF = float("inf")

# Example 1
print("######Example 1######")
n = 5  # the number of vertices
W = [  # adjacency matrix
    [INF, INF, INF, INF, INF, INF],
    [INF, 0, 7, 4, 6, 1],
    [INF, INF, 0, INF, INF, INF],
    [INF, INF, 2, 0, 5, INF],
    [INF, INF, 3, INF, 0, INF],
    [INF, INF, INF, INF, 1, 0],
]
touch = [-1] * (n + 1)
length = [-1] * (n + 1)

F = dijkstra(n, W)
print(F)


# # Example 2 - Your Custom Case
print("######Example 2 #######")
# # Insert your example here
n = 5
W = [  # adjacency matrix
    [INF, INF, INF, INF, INF, INF],
    [INF, 0, 6, 1, 4, INF],
    [INF, 1, 0, 7, 1, INF],
    [INF, 4, 1, 0, 4, 2],
    [INF, INF, 1, 2, 0, 5],
    [INF, INF, INF, 2, 5, 0],
]
touch = [-1] * (n + 1)
length = [-1] * (n + 1)
# raise NotImplementedError("Complete your example.")

F = dijkstra(n, W)
print(F)

