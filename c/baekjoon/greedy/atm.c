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
	int n=5;
	int i;
	int arr[5] = {3, 1, 4, 3, 2};
	int *ptr=arr;

	sortnum(n, ptr);
	for(i=0; i<n; i++)
	{
		printf("%d ", arr[i]);
	}
	return 0;
}
