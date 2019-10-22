#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//"BACDE", "CBADF", "AECB", "DBA"
int solution(char* skill, char* skill_trees[], size_t skill_trees_len)
{
	int answer = 0;
	int i, j;
	for(i=0; i<skill_trees_len; i++)
	{
		//printf("%s \n", skill_trees[i]);
		//printf("%d \n", strlen(skill_trees[i]));
		char nskill[4];
		strcpy(nskill, skill);
		printf("nskill 값은 : %s \n", nskill);
		printf("skill 값은 : %s \n", skill);
		for(; *skill_trees[i] != '\0'; skill_trees[i]++)
		{
			printf("%c ", *(skill_trees[i]+1));
			if(strchr(nskill, *skill_trees[i] == NULL))
			{
				printf("%c 패스됨 \n", *skill_trees[i]);
				continue;
			}
			else if(strchr(nskill, *skill_trees[i]) && *skill_trees[i] == nskill[0])
			{
				strcpy(nskill, nskill+1);
				printf("%c 해당됨 \n", *skill_trees[i]);
			}
			else
			{
				printf("%c 엘스됨 \n", *skill_trees[i]);
				break;
			}
			if(*(skill_trees[i]+1) == '\0')
			{
				answer += 1;
				printf("%d 여기는 0", i);
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
