#d = [1,3,2,5,4]
#bud = 9
d = [2,2,3,3]
bud = 10

def solution(d, bud):
    d.sort()
    cnt = 0
    for i in d:
        if bud>=i:
            bud -= i
            cnt += 1
    return cnt

print(solution(d, bud))
