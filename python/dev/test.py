def palindrome(word):
	l = list(word)
	if l != l[::-1]:
		raise NotPalindromeError('회문이 아닙니다')
	print(word)

try:
	word = input("회문 판별 문자열 입력: ")
	palindrome(word)
except NotPalindromeError as e:
	print(e)
