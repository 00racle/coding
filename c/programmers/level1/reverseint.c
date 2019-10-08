#include <stdio.h>
#include <stdlib.h>

int* solution(long long n)
{
	int i;
	int len = sizeof(n);
	int* answer = (int*)malloc(sizeof(int)*len);
	for(i=0; i<len; i++)
	{
		answer[i] = n%10;
		n /= 10;
	}
	return answer;
}

int main(void)
{
	int n, i;
	printf("정수 n입력: ");
	scanf("%d", &n);
	int* ret = solution(n);
	for(i=0; i<5; i++)
	{
		printf("%d ", ret[i]);
	}
	printf("\n");
	return 0;
}
