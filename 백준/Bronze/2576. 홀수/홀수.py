number=[]
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        number.append(a)
if number:
    print(sum(number))
    print(min(number))
else:
    print(-1)
