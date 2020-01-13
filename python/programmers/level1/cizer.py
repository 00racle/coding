s = "AaZz"  #ZzYy 가 나와야 하는데 Zzsy가 나
n = 25

#abcdefghijklmnopqrstuvwxyz
#12345678901234567890123456
# Z = 90, z = 122, s = 115
# A=65(91), a=97(122), Z=90(115), z=122(147)
def solution(s, n):
    b = list(map(lambda x: ord(x)+n, list(s)))
    for i in range(len(b)):
        if b[i] == 32+n:
            b[i] = b[i]-n
        elif b[i] not in range(65, 91) and b[i] not in range(97, 123):
            b[i] = b[i]-26
    c = list(map(lambda x: chr(x), b))
    return ''.join(c)


print(solution(s, n))
