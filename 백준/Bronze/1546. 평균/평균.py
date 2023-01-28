sub = int(input())
a = list(map(int,input().split()))
b = max(a)
c = []

for i in a:
    d = i / b * 100
    c.append(d)

print(sum(c)/sub)