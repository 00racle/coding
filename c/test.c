#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char *string = "0xFF";
	char *stop;
	int radix;
	long value;

	radix = 16;

	value = strtol(string, &stop, radix);

	printf("%ld 개의 문자가 변환되었습니다. \n", stop-string);
	printf("16진수 %s를 숫자로 변환하면 %ld입니다. \n",string, value);
	return 0;
}
