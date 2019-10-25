#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* solution(int n)
{
	char* answer = (char*)malloc(sizeof(char)*100);
	//char str1[] = "수박";
	//char str2[] = "수";
	int len = n/2;
	int i;

	if(n%2 == 0)
	{
		for(i=0; i<len; i++){
			strcat(answer, "수박");
		}
	}
	else
	{
		for(i=0; i<len; i++){
			strcat(answer, "수박");
		}
		strcat(answer, "수");
	}
	return answer;
}

int main(void)
{
	int n;
	printf("정수 n입력: ");
	scanf("%d", &n);
	printf("결과값 s: %s \n", solution(n));
	return 0;
}
