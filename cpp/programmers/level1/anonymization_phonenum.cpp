#include <iostream>
#include <string>

using namespace std;

string solution(string p)
{
	string answer = "";
	answer = p;
	int l = p.size();
	for(int i=0; i<l-4; i++)
	{
		answer[i] = '*';
	}
	return answer;
}

int main(void)
{
	string p = "01026531417";
	string answer = "";
	answer = solution(p);
	cout<<"결과 값: "<<answer<<endl;
	return 0;
}
