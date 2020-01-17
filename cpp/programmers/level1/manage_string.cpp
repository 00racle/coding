#include <iostream>
#include <string>

using namespace std;

bool solution(string s)
{
	bool answer = true;
	if(s.size() != 4 && s.size() != 6)
	{
		answer = false;
		return answer;
	}
	else
	{
		for(int i=0; i<s.size(); i++)
		{
			if(isdigit(s[i]) == 0)
			{
				answer = false;
				break;
			}
		}
	}
	return answer;
}

int main(void)
{
	string s = "1234";
	bool ret;
	ret = solution(s);
	cout<<"결과 값은: "<<ret<<endl;
	return 0;
}
