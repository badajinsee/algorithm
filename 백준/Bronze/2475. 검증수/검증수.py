num = list(map(int,input().split()))

number = []

for i in num:
    a = i ** 2
    number.append(a)
print(sum(number)%10)