n, m = map(int, input().split())
num = list(map(int, input().split()))

total = 0
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if(num[i] + num[j] + num[k] > m):
                continue
            else:
                total = max(total ,num[i] + num[j] + num[k])

print(total)