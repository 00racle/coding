#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool solution(int x)
{
	bool answer = true;
	int slen, i;
	int sum=0;
	char* s1 = (char*)malloc(sizeof(char)*100);
	sprintf(s1, "%d", x);
	slen = strlen(s1);
	for(i=0; i<slen; i++)
	{
		sum += s1[i]-48;
	}
	/*if(x%sum == 0)
	{
		answer = true;
	}
	else
	{
		answer = false;
	}*/
	answer = x%sum == 0 ? true : false;
	
	return answer;
}

int main(void)
{
	int x;
	printf("정수 입력: ");
	scanf("%d", &x);
	printf("결과 값은: %s \n", solution(x) ? "true" : "false");
	return 0;
}
