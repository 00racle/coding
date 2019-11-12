#include <stdio.h>

int main(void)
{
	int n, k;
	int i;
	int arr[10];

	printf("n과k 그리고 동전 입력 \n");
	scanf("%d %d", &n, &k);
	for(i=0; i<10; i++)
	{
		scanf("%d", &arr[i]);
	}
	/*
	printf("n : %d, k : %d \n", n, k);
	printf("arr는 : ");
	for(i=0; i<10; i++)
	{
		printf("%d ", arr[i]);
	}*/
	printf("\n");
	return 0;
}
