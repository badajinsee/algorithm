a, b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))
e = []
f = []

e.append(c)
f.append(d)

num = list(set(c)-set(d))
num_2 = list(set(d)-set(c))

print(len(num)+len(num_2))
