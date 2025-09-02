#예시1
def sum1(A, n):
    sum = 0
    for i in range(0, n-1):
        if A[i] % 2 == 0:
            sum = sum + A[i]
    return sum
A = [2,4,6,8,10,12]

print(sum1(A,len(A)))

#예시2
def sum2(A, n):
    sum=0
    for i in range(0, n):
        for j in range(i, n):
            sum = sum + A[i] * A[j]
    return sum
A = [1,2,3,4,5,6]
print(sum2(A, len(A)))