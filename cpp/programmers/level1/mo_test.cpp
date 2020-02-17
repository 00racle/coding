#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers);

int main(void)
{
	vector<int> answers;
	vector<int> ret;
	int num;
	cout<<"answers입력: ";
	for(int i=0; i<5; i++)
	{
		cin>>num;
		answers.push_back(num);
	}
	
	ret = solution(answers);
	cout<<"결과 값은: ";
	for(int i=0; i<ret.size(); i++)
	{
		cout<<ret[i]<<" ";
	}
	cout<<endl;
	return 0;
}

vector<int> solution(vector<int> answers)
{
	vector< vector<int> > su1 = {
		{1,2,3,4,5},
		{2,1,2,3,2,4,2,5},
		{3,3,1,1,2,2,4,4,5,5}
	};
	int length = answers.size();
	int cnt = 0;
	vector< vector<int> > su2;
	su2.reserve(3);
	vector<int> answer;
	for(int i=0; i<3; i++)
	{
		int m = length/su1[i].size();
		int n = length%su1[i].size();
		for(int j=0; j<m; j++)
		{
			su2[i].insert(su2[i].end(), su1[i].begin(), su1[i].end());
		}
		su2[i].insert(su2[i].end(), su1[i].begin(), su1[i].begin() + n);
	}
	for(int i=0; i<3; i++)
	{
		cnt = 0;
		for(int j=0; j<length; j++)
		{
			if(answers[j] == su2[i][j])
			{
				cnt += 1;
			}
		}
		answer.push_back(cnt);
	}
	return answer;
}
