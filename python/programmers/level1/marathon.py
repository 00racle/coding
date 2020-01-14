import time
import collections

#p = ["leo", "kiki", "eden"]
#c = ["eden", "kiki"]
#p = ["marina", "josipa", "nikola", "vinko", "filipa"]
#c = ["josipa", "filipa", "marina", "nikola"]
p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
start_time=time.time()
'''
def solution(p, c):
    ret = ''
    for j in p:
        if j in c:
            c.remove(j)
        else:
            ret += j
    return ret

'''
def solution(p, c):
    ret = ''
    p.sort()
    c.sort()
    ret = p[-1]
    for i in range(len(c)):
        if p[i] != c[i]:
            ret = p[i]
            break
    return ret
print(solution(p, c))
# ------- 다른 사람 풀이 ------------
'''
def solution(p, c):
    answer = collections.Counter(p) - collections.Counter(c)
    print(answer)
    return list(answer.keys())[0]

def solution(p, c):
    answer = ''
    temp = 0
    dic = {}
    for part in p:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in c:
        temp -= hash(com)

    answer = dic[temp]

    return answer

'''


print(solution(p, c))
end_time = time.time()
print("Runtime: %0.8f"%(end_time - start_time))
