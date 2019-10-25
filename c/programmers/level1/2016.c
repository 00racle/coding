#include <stdio.h>
#include <stdlib.h>

char* solution(int a, int b)
{
	int i;
	int sum = 0;
	int ret;
	char* answer = (char*)malloc(sizeof(char)*4);
	int month[13] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	char* week[7] = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};
	for(i=0; i<a; i++)
	{
		sum += month[i];
	}
	sum += b;
	ret = sum%7;
	answer = week[ret];

	return answer;
}

int main(void)
{
	int a, b;
	printf("월 입력: ");
	scanf("%d", &a);
	printf("일 입력: ");
	scanf("%d", &b);
	printf("%d월 %d일 의 요일은: %s \n", a, b, solution(a, b));
	return 0;
}
