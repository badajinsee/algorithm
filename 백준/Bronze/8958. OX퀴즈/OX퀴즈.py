# ox 퀴즈

T = int(input())

for t in range(1,T+1):
    quiz = input()
    cnt = 0
    cmo = 0
    for i in quiz:
        if i == 'O' :
            cnt += 1
        else:
            cnt = 0
        cmo += cnt
    print(cmo)
