n, m = input().split()
a = []
b = []

for i in n:
    a.append(i)
for j in m:
    b.append(j)

c = list(map(int,a))
d = list(map(int,b))

print(sum(c)*sum(d))