a = int(input())

for i in range(a):
    c = []
    b = input()

    for j in b:
        if j == '(':
            c.append(j)
            
        elif j == ')':
            if c:
                c.pop()

            # c에 아무것도 없는 경우 
            else:
                print('NO')
                break
    else:
        if len(c) == 0:
            print('YES')
        else:
            print('NO')