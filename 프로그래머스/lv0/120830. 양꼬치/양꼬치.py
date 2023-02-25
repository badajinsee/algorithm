def solution(n, k):
    a = n * 12000
    b = k * 2000
    answer = a + b - (n//10 * 2000)
    return answer

