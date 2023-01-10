T = int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    a = sum(numbers)
    b = len(numbers)
    print(f'#{t} {round(a/b)}')