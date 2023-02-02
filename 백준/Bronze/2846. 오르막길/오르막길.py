n = int(input())
a = list(map(int,input().split()))
b = 0
c = []
for i in range(n-1):
    if a[i] < a[i+1]:
        b += a[i+1] - a[i]
    else:
        c.append(b)
        b = 0
c.append(b)
print(max(c))