a, b, c = list(map(int,input().split()))

if a == b == c :
    print(10000 + a * 1000) # 같은 눈 3 개 
elif a == b or a == c:
    print(1000 + a * 100)  # 같은 눈 2개 (a,b)(a,c)
elif b == c:
    print(1000 + b * 100) # 같은 눈 2개 (b,c)
else:
    print(max(a, b, c)*100) # 그 외