a = int(input())
b = list(map(int,input().split()))
c = []
d = 0

for i in range(a):
    if b[i] in c :
        d += 1 
    else:
        c.append(b[i])
print(d)