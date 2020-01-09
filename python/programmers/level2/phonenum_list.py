#p = ["119", "97674223", "1195524421"]
#p = ["123", "456", "789"]
#p = ["12", "123", "1234", "567", "88"]
p = ["97674223", "1195524421", "119"]

def solution(p):
    # 시간 통과 못함
    '''
    answer = True
    for i in range(len(p)):
        l = len(p[i])
        for j in p[i+1:]:
            if(l < len(j) and p[i] == j[:l]):
                print(p[i], j[:l])
                answer = False
                break
    '''
    '''
    answer = True
    for i in range(len(p)):
        if p[i] in list(map(lambda x: x[:len(p[i])], p[i+1:])):
            answer = False
            break
    return answer

    '''
    answer = True
    for i in p:
        p1 = p[:]
        p1.remove(i)
        print(p, p1)
        if i in list(map(lambda x: x[:len(i)], p1)):
            answer = False
        

    return answer

print(solution(p))
