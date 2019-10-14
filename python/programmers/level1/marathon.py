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
print(solution(p, c))

def solution(p, c):
    ret = ''
    for j in p:
        if j in c:
            I = c.index(j)
            del c[I]
        else:
            ret += j
    return ret
print(solution(p, c))
'''

def solution(p, c):
	print(collections.Counter(p))
	print(collections.Counter(c))
	answer = collections.Counter(p) - collections.Counter(c)
	print(answer)
	print(list(answer.keys()))

solution(p, c)
end_time = time.time()
print("Runtime: %0.8f"%(end_time - start_time))
