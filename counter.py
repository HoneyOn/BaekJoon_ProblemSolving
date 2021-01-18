from collections import Counter

N = int(input())
A = input().split(' ')
A = [int(x) for x in A]
M = int(input())
B = input().split(' ')
B = [int(x) for x in B]

counter = Counter(A)

for i in range(len(B)):
    print(counter[B[i]], end=' ')
