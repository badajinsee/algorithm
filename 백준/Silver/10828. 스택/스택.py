# 스택 
import sys
a = int(sys.stdin.readline())
c = []

for i in range(a):
    b = sys.stdin.readline().split()  # push 1 입력시 b[0] = push b[1] = 1 

    if b[0] == 'push':
        c.append(b[1])
    
    elif b[0] == 'pop':
        if not c : # c가 없다면 
            print(-1)
        else:
            print(c.pop())
    
    elif b[0] == 'empty':
        if not c :
            print(1)
        else:
            print(0)

    elif b[0] == 'size':
        print(len(c))

    elif b[0] == 'top':
        if not c :
            print(-1)
        else:
            print(c[-1]) #스택 핫케이크 생각하기 먼저 구어진게 올라가는것이기 때문에 나중에 구운게 맨 위로 그래서 -1