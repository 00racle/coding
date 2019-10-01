#include <stdio.h>
#include <stdlib.h>

char* solution(int num)
{
	char* answer = (char*)malloc(sizeof(char)*4);
	if(num%2 == 0)
		answer = "Even";
	else
		answer = "Odd";
	return answer;
}
// 다른 사람 풀이
// char* solution(int num){
//		return num%2==0 ? "Even":"Odd";
//		}

int main(void)
{
	int num;
	printf("정수 num입력: ");
	scanf("%d", &num);
	char* ret = solution(num);
	printf("결과 값은 : %s \n", ret);
	return 0;
}
