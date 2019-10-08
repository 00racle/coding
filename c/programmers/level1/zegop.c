#include <stdio.h>
#include <stdlib.h>

// 0, 1, 4, 5, 6, 9

long long solution(long long n)
{
	long long answer = 0;
	int i;
	int s;
	if(n%1 == 0 || n%1 == 1 || n%1 == 4 || n%1 == 5 || n%1 == 6 || n%1 == 9)
	{
		for(i=0; i<n/2; i++)
		{
			if(i*i == n)
			{
				s = i;
				break;
			}
		}
		answer = (s+1)*(s+1);
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
