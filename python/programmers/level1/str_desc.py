import time


start_time = time.time()

s = 'Zbcdefg'
'''
def solution(s):
    ret = []
    a = list(map(ord, list(s)))
    for i in range(len(a)):
        ret.append(max(a))
        a.remove(max(a))

    return ''.join(map(chr, ret))

'''
# 다른사람 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))
print(solution(s))
end_time = time.time()

print("Runtime : %0.6f \n"%(end_time - start_time))


