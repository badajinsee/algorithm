import sys
a = int(sys.stdin.readline())
c = []

for i in range(a):
    b = input().strip()
    
    if b not in c:
        c.append(b)

c.sort() # 정렬 
c.sort(key=lambda x:len(x)) # 문자열 길이 순으로 정렬 

for i in range(len(c)):
    print(c[i])
