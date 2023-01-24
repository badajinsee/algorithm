while True:
    try:
        print(input())
    except EOFError: #EOFError > 문자의 끝 
        break
