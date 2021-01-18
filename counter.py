from collections import Counter

N = int(input())

#domain 숫자들 담기
A = list(map(int, input().split()))
M = int(input())

#갯수를 셀 숫자들 담기
B = list(map(int, input().split()))

#counting class 생성
counter = Counter(A)

for i in range(len(B)):
    print(counter[B[i]], end=' ')
