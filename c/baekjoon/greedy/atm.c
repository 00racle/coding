#include <stdio.h>
#include <stdlib.h>				//malloc, free 함수가 선언된 헤더 파일
#include <string.h>

int sortnum(int n, int *arr)
{
	int i, j;
	int temp=0;
	for(i=1; i<n; i++)
	{
		for(j=i; j>=0; j--)
		{
			if(arr[j] < arr[j-1])
			{
				temp = arr[j];
				arr[j] = arr[j-1];
				arr[j-1] = temp;
			}
			else
				continue;
		}
	}
}

int main(void)
{
	int n;
	int i;
	int arr[1001];
	int sum1=0;
	int sum2=0;
	scanf("%d", &n);
	for(i=0; i<n; i++)
		scanf("%d", &arr[i]);
	sortnum(n, arr);
	for(i=0; i<n; i++)
	{
		sum1 += arr[i];
		sum2 += sum1;
	}
	printf("%d", sum2);
	return 0;
}
