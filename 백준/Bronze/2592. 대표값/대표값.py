import statistics
a = []

for i in range(10):
    num = int(input())
    a.append(num)

print(sum(a)//10)
print(statistics.mode(a))
