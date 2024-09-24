def merge(h, m, U, V, S):
    assert sorted(U) == U
    assert sorted(V) == V

    i = j = k = 0
    # Complete the code here
    while i < h and j < m:
        if U[i] < V[j]:
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1

    if i > j:
        for idx in range(j, m):
            S[k] = V[idx]
            k += 1
    else:
        for idx in range(i, h):
            S[k] = U[idx]
            k += 1


def mergesort(n, S):
    h = n // 2
    m = n - h
    if n > 1:
        # Complete the code here
        U = S[:h]
        V = S[h:]
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)


# Example 1 for 'merge()'
print("######Example 1 for 'merge()'######")
U = [17, 19, 39, 41, 73]  # sorted
V = [16, 22, 66, 94, 98]  # sorted
h = len(U)
m = len(V)
S = [-1] * (h + m)
merge(h, m, U, V, S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 2 - Your Custom Case for 'merge()'
print("######Example 2 for 'merge()'######")
# Insert your example here
U = [3, 10, 17, 21, 32, 52]
V = [15, 27, 35, 54, 64]
h = len(U)
m = len(V)
S = [-1] * (h + m)
# raise NotImplementedError("Complete your example.")
merge(h, m, U, V, S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 1 for 'mergesort()'
print("######Example 1 for 'mergesort()'######")
S = [22, 98, 17, 16, 19, 73, 94, 41, 39, 66]
mergesort(len(S), S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 2 - Your Custom Case for 'mergesort()'
print("######Example 2 for 'mergesort()'######")
# Insert your example here
S = [17, 456, 19, 21, 83, 72, 1, 55, 20]
# raise NotImplementedError("Complete your example.")
mergesort(len(S), S)
print("S:", S)
print(f"{'-'*20}\n")
