h, m = list(map(int,input().split()))
a = int(input())

m += a
h += m //60

m %= 60
h %= 24 
print(h,m)