#include <stdio.h>
#include <stdlib.h>

int solution(long num)
{
	int answer = 0;
	while(num != 1)
	{
		if(num%2 == 0)
		{
			num = num/2;
			answer += 1;
		}
		else
		{
			num = num*3+1;
			answer += 1;
		}
		if(answer >= 500)
		{
			answer = -1;
			break;
		}

	}
	return answer;
}

int main(void)
{
	int num;
	printf("정수 num입력: ");
	scanf("%d", &num);
	printf("결과 값: %d \n", solution(num));
	return 0;
}
