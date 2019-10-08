#include <stdio.h>
#include <stdlib.h>

int solution(int n)
{
	int answer = 0;
	int a=0, b=1;
	int i;

	if(n == 1)
	{
		return n;
	}
	else
	{
		for(i=0; i<n-1; i++)
		{
			answer = a+b;
			a = b;
			b = answer;
		}
	}

	return answer%1234567;
}

int main(void)
{
	int n;
	printf("정수 n입력: ");
	scanf("%d", &n);
	printf("결과 값은: %d \n", solution(n));
	return 0;
}
