c = []
for i in range(10):
    a = int(input())
    b = a % 42
    c.append(b)
    d = set(c)
print(len(d))