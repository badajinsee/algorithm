a = int(input())
w =[1,2,3]

for i in range(a):
    b,c = map(int,input().split())
    d = w.index(b)
    c = w.index(c)
    w[d], w[c] = w[c],w[d]
print(w[0])