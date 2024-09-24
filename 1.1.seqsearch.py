def seqsearch(n, S, x):
    location = 0

    # Complete the code here
    for i in range(n):
        if S[i] == x:
            location = i
            return location
    if location == 0:
        location = -1

    return location


# Example 1 - Best Case
print("######Example 1######")
S = [10, 7, 11, 5, 13, 8]
x = 10
location = seqsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")

# Example 2 - Worst Case
print("######Example 2######")
S = [10, 7, 11, 5, 13, 8]
x = 6
location = seqsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")

# Example 3 - Specific Case
print("######Example 3######")
S = [10, 7, 11, 5, 13, 8]
x = 5
location = seqsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")

# Example 4 - Your Custom Case
print("######Example 4######")
# Insert your example here
S = [3, 1, 10, 4, 9, 8, 7, 2, 6, 5, 0, 11]
x = 7
# raise NotImplementedError("Complete your example.")
location = seqsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")
