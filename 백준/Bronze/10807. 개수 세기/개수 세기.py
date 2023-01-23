a = int(input())
b = list(map(int,input().split()))
c = int(input())
count = 0
for i in b:
    if c == i:
        count += 1
print(count)
