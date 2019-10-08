#s = "1 2 3 4"
s = "-1 -2 -3 -4"

def solution(s):
    answer = ""
    l = list(map(int , s.split(" ")))
    answer += str(min(l))+" "
    answer += str(max(l))
    return answer


print(solution(s))
