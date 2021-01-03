#input의 제한이 주어져있지 않고,
#알아서 End Of File이나 입력창을 끝내야하는 경우

#1) stdin을 이용
import sys
for line in sys.stdin:
    a,b = map(int,line.split())
    print(a+b)

#2) 예외처리
try:
    while True:
        a, b = map(int, input().split())
        print(a + b)
except:
    exit()