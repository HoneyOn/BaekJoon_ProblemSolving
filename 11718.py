#1) 예외처리
while True:
    try:
        print(input())
    except EOFError:
        break
        
#2) sys.stdin
import sys
for i in range(101):
    string = sys.stdin.readline()
    print (string, end ='')
        
