w = []
k = []

for i in range(10):
    a = int(input())
    w.append(a)
for j in range(10):
    b = int(input())
    k.append(b)

w = sorted(w,reverse=True)
k = sorted(k,reverse=True)

w_sum = 0
k_sum = 0

for n in range(3):
    w_sum += w[n]
for m in range(3):
    k_sum += k[m]

print (w_sum, k_sum)