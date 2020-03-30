#include <iostream>
#include <string>

using namespace std;

bool solution(string s);
int main(void)
{
	string s;
	cout<<"문자열 입력: ";
	cin>>s;

	cout<<"결과 값은: "<<solution(s)<<endl;
	return 0;
}

bool solution(string s)
{
	int pcnt=0;
	int ycnt=0;

	for(int i=0; i<s.size(); i++)
	{
		if(s[i] =='P' || s[i] == 'p')
		{
			pcnt += 1;
		}
		else if(s[i] == 'Y' || s[i] == 'y')
		{
			ycnt += 1;
		}
	}
	return pcnt == ycnt;
}
