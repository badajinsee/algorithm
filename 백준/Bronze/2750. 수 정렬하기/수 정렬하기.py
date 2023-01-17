a = int(input())
number = []

for i in range(a):
    number.append(int(input()))
number.sort()

for i in number:
    print(i)