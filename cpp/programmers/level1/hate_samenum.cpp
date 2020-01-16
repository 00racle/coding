#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr)
{
	vector<int> answer;
	int temp = 10;
	for(int i=0; i<arr.size(); i++)
	{
		if(arr[i] != temp)
		{
			temp = arr[i];
			answer.push_back(arr[i]);
		}
	}
	return answer;
}

int main(void)
{
	vector<int> arr = {1,1,3,3,0,1,1};
	vector<int> ret;

	ret = solution(arr);
	for(int i=0; i<ret.size(); i++)
	{
		cout<<ret[i]<<" ";
	}
	cout<<endl;
	return 0;
}
