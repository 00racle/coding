#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// 0, 1, 4, 5, 6, 9
// 2, 3, 7, 8
// sqrt(

long long solution(long long n)
{
	long long answer = 0;
	if(sqrt(doubel(n)) == 
	/*
	int i;
	int s;
	if(n%10 == 2 || n%10 == 3 || n%10 == 7 || n%10 == 8){
		answer = -1;
	}
	else{
		for(i=1; i<n/2; i++){
			if(i*i == n){
				s = i;
				break;
			}
		}
		answer = (s+1)*(s+1);
	}
	*/
	

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
