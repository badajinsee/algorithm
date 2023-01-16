n = int(input())

a = 0 
result = 0 
k = list(map(int, input().split()))

for i in range(n):
    if k[i] == 1:
        a += 1 
        result += a 
    else :
        a = 0
print(result)