total = 0 

for i in range(5): # 5번 
    score = int(input()) # 점수 입력값 
    if score < 40 : # score가 40점 미만이면 
        score = 40 # 40점 

    total += score # total+score 
print(total//5) # 몫만 