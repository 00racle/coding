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
<<<<<<< HEAD
	int arr[3][9];
	int i, j;

	for(i=0; i<3; i++)
		for(j=0; j<9; j++)
			arr[i][j] = (i+2) * (j+1);


	for(i=0; i<3; i++)
	{
		for(j=0; j<9; j++)
			printf("%4d", arr[i][j]);
		printf("\n");
	}
=======
	int a, b;

	printf("정수 두개 입력하세요!");
	scanf("%d %d", &a, &b);

	printf("결과값은 : %d \n", Solution(a, b));
>>>>>>> 9453cf932445a1b88cab0129127be373671c41f3
	return 0;
}
