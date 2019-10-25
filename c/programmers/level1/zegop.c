#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long long solution(long long n)
{
	long long answer = 0;

	if(sqrt(n) - (int)sqrt(n) == 0) 
	{
		answer = (sqrt(n)+1)*(sqrt(n)+1);
	}
	else
	{
		answer = -1;
	}
	return answer;
}

int main(void)
{
	long long n;
	printf("정수 n입력: ");
	scanf("%lld", &n);
	printf("결과 값은: %lld \n", solution(n));
	return 0;
}
