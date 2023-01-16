N, X = list(map(int,input().split())) 
a = list(map(int,input().split())) # 리스트 형태로 들어감 
for i in range(N): # n-1번 까지 반복 
    if a[i] < X: #  x 값 보다 작은 값 출력 
        print(a[i], end= " ")