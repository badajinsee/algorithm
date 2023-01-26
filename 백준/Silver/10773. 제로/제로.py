import sys
input = sys.stdin.readline

num = int(input())
b = []
for i in range(num):
    a = int(input())
    
    if a == 0: 
        b.pop()
    else:
        b.append(a)
print(sum(b))