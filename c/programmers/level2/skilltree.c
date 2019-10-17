#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int solution(char* skill, char* skill_trees[], size_t skill_trees_len)
{
	int answer = 0;
	int i, j;
	for(i=0; i<skill_trees_len; i++)
	{
		//printf("%s \n", skill_trees[i]);
		//printf("%d \n", strlen(skill_trees[i]));
		for(j=0; j<strlen(skill_trees[i]); j++)
		{
			//printf("%c ", skill_trees[i][j]);
			if(
		}
		printf("\n");
	}

	return answer;
}

int main(void)
{
	char skill[] = "CBD";
	char* skill_trees[] = {"BACDE", "CBADF", "AECB", "DBA"};
	printf("결과값: %d \n", solution(skill, skill_trees, sizeof(skill_trees)/sizeof(skill_trees[0])));
	//printf("사이즈는: %d \n", sizeof(skill_trees[1]));
	return 0;
}
