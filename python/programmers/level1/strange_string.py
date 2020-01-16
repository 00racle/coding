#s = "try  hello world"
#s = "try hello world strys try"
s = "sp  ace"

def solution(s):
    answer = ""
    l = s.split(" ")
    for i in l:
        for j in range(len(i)):
            if j%2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j]
        answer += " "

    answer = answer.strip()

    return answer + "."

            
print(solution(s))
