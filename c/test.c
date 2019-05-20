#include <stdio.h>
#include <string.h>

int Solution(int a, int b)
{
	int sum=0;
	int i;
	if(a>b)
	{
		for(i=b; i<=a; i++)
			sum += i;
		return sum;
	}
	else
	{
		for(i=a; i<=b; i++)
			sum += i;
		return sum;
	}
}


int main(void)
{
	int a, b;

	printf("정수 두개 입력하세요!");
	scanf("%d %d", &a, &b);

	printf("결과값은 : %d \n", Solution(a, b));
	return 0;
}
