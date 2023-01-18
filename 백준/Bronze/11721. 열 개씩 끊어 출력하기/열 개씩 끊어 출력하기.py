text = input()

for i in range(0,len(text),10): # 0부터 텍스트 길이까지 10자리까지 (시작, 종료, step)
    print(text[i:i+10]) # 시작값 [0:10] > [10:20] 10개 문자열 출력 
