a = [3, -1, 9, 2, 12]
def arrayMax(n, A):
    currentmax = a[0]
    for i in range(1, n-1):
        if currentmax < a[i]:
            currentmax = a[i]
    return currentmax
print(arrayMax(len(a), a))