#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//"BACDE", "CBADF", "AECB", "DBA"
int solution(char* skill, char* skill_trees[], size_t skill_trees_len)
{
	int answer = 0;
	int i;
	for(i=0; i<skill_trees_len; i++)
	{
		char nskill[10];
		strcpy(nskill, skill);
		for(; *skill_trees[i] != '\0'; skill_trees[i]++)
		{
			if(*(skill_trees[i]+1) == '\0')
			{
				answer += 1;
			}
			if(strchr(nskill, *skill_trees[i]) == NULL)
			{
				continue;
			}
			else if(strchr(nskill, *skill_trees[i]) && *skill_trees[i] == nskill[0])
			{
				strcpy(nskill, nskill+1);
			}
			else
			{
				break;
			}
		}
	}
	return answer;
}

int main(void)
{
	//char skill[] = "CBD";
	char skill[] = "DA";
	//char* skill_trees[] = {"BACDE", "CBADF", "AECB", "DBA"};
	char* skill_trees[] = {"ABCDE", "UCBADF", "ACEB", "BDA"};
	printf("결과값: %d \n", solution(skill, skill_trees, sizeof(skill_trees)/sizeof(skill_trees[0])));
	return 0;
}
