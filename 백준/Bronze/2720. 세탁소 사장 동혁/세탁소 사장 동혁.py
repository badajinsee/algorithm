c = [25,10,5,1]
T = int(input())

for t in range(1,T+1):
    money = int(input())
    li = []

    for i in c:
        li.append(money // i)
        money = money % i
    print(*li)