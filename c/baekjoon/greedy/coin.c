#include <stdio.h>

int minnum(int n, int k, int *lst[])
{

}

int main(int n, int k)
{
	int i;
	int lst[10];
	scanf("%d %d", &n, &k);
	printf("n은 : %d \n", n);
	printf("k는 : %d \n", k);
	for(i=0; i<10; i++)
	{
		scanf("%d", &lst[i]);
	}
	for(i=0; i<10; i++)
	{
		printf("%d ", lst[i]);
	}
	return 0;
}

