for _ in range (int(input())):
    text = input().split()
    for i in text:
        print(i[::-1], end= ' ')
