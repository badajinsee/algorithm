train = []
c = 0
for i in range(4):
    a, b = map(int,input().split())
    c = c - a + b
    train.append(c)
print(max(train))