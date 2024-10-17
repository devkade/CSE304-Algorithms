import time


def bin(n, k):
    if k == 0 or n == k:
        return 1
    else:
        # Complete the code here
        return bin(n - 1, k - 1) + bin(n - 1, k)


# Example 1
print("######Example 1######")
n = 15
k = 7
stime = time.time()
answer = bin(n, k)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime, 5))
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######")
n = 30
k = 10
stime = time.time()
answer = bin(n, k)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime, 5))
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case
print("######Example 3######")
# Insert your example here
n = 31
k = 10
# raise NotImplementedError("Complete your example.")
stime = time.time()
answer = bin(n, k)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime, 5))
print(f"{'-'*20}\n")
