b = []
for i in range(5):
    a = list(map(int,input().split()))
    b.append(sum(a))
print(b.index(max(b))+1,max(b))