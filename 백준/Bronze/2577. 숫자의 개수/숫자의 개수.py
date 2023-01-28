a = int(input())
b = int(input())
c = int(input())

d = str(a*b*c)
co = 0
for i in range(10):
    co = d.count(str(i))
    print(co)
