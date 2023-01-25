b = []
cnt =0
for i in range(10):
    num = int(input())
    a = num % 42 
    b.append(a)
c = set(b)
print(len(c))