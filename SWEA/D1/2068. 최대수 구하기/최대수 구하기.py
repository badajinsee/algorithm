T = int(input())

for t in range(1,T+1):
    a = list(map(int,input().split()))
    b = max(a)
    print(f'#{t} {b}')