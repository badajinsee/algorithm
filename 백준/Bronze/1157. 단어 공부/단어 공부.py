# 단어 공부 

a = input().upper()
s = list(set(a))
b = []

for i in s:
    c = a.count(i)
    b.append(c)
if b.count(max(b)) >= 2:
    print('?')
else:
    print(s[(b.index(max(b)))]) # 기억해두자 