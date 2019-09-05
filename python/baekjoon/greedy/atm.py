n = 5
arr = [3, 1, 4, 3, 2]
#[1, 2, 3, 3, 4]

def solution(n, arr):
    sum1 = 0
    sum2 = 0
    arr.sort()
    for i in arr:
        sum1 += i
        sum2 += sum1

    print(sum2)

solution(n, arr)
