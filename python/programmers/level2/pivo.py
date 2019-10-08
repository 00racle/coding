# pivo = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
#        0  1  2  3  4  5  6  7   8   9
n = int(input("정수 n입력: "))

def solution(n):
    a = 0
    b = 1
    if n == 0 or n == 1:
        return n
    else:
        for i in range(n-1):
            pi = a + b
            a = b
            b = pi

    return pi%1234567

print(solution(n))
