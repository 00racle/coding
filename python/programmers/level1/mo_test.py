answers = [1,2,3,4,5]

def solution(answers):
    s1 = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    s2 = []
    ret = []
    for i in s1:
        s2.append(i*(len(answers)//len(i)) + i[:len(answers)%len(i)])

    for i in s2:
        cnt = 0
        for j in range(len(answers)):
            if answers[j] == i[j]:
                cnt += 1

        ret.append(cnt)

    m = max(ret)
    return [ret.index(m)+1] if ret.count(m) == 1 else [i+1 for i in range(len(ret)) if ret[i] == m]

print(solution(answers))
