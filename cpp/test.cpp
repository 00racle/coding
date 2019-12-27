#include <iostream>
#include <ctime>
#include <conio.h>

using namespace std;

void Initialize();				// 초기화
void Shuffle(int nCount);		// 입력된 카운트만큼 셔플
void Swap(int* n0, int* n1);	// 스왑
void Print();					// 출력
bool Complete();				// 퍼즐 완성 여부 확인
int GetIndex(int nNumber);		// 해당 숫자의 인덱스 반환
void Play(int currentIndex);	// 게임 플레이

const int KEY_LEFT = 75;
const int KEY_RIGHT = 77;
const int KEY_UP = 72;
const int KEY_DOWN = 80;

int nNumbers[25] = {};
int nSize = sizeof(nNumbers) / sizeof(nNumbers[0]);

void main()
{
	Initialize();
	Shuffle(100);

	while(!Complete())
	{
		Print();
		int currentIndex = GetIndex(0);
		Play(currentIndex);
	}
}

// 초기화
void Initialize()
{
	for(int i=0; i<nSize; i++)
	{
		nNumbers[i] = i;
	}
}

// 입력된 카운트만큰 셔플
void Shuffle(int nCount)
{
	srand(time(NULL));
	for(int i=0; i<nCount; i++)
	{
		int nFirst = rand() % nSize;
		int nSecond = rand() % nSize;

		Swap(&nNumbers[nFirst], &nNumbers[nSecond]);
	}
}

void Swap(int* n0, int* n1)
{
	int temp = *n0;
	*n0 = *n1;
	*n1 = temp;
}
// 출력
void Print()
{
	system("cls");
	cout<<"============< 퍼즐 게임 >=============="<<endl;
	for(int i=0; i<nSize; i++)
	{
		if(i%5 == 0) cout<<endl;
		cout<<nNumbers[i] <<'\t';
	}
}
// 퍼즐 완성 여부 확인
bool Complete()
{
	for(int i=0; i<nSize - 1; i++)
	{
		if(nNumbers[i] != i+1) return false;
	}
	return true;
}
// 해당 숫자의 인덱스 반환
int GetIndex(int nNumber)
{
	for(int i=0; i<nSize; i++)
	{
		if(nNumbers[i] == nNumber) return i;
	}
	return -1;
}
// 게임 플레이
void Play(int currentIndex)
{
	int nInput = getch();
	if(nInput == 224)
	{
		nInput = getch();

		switch(nInput)
		{
			case KEY_LEFT:
				if(currentIndex % 5 !=0)
				{
					Swap(&nNumbers[currentIndex], &nNumbers[currentIndex +1]);
				}
				break;

			case KEY_RIGHT:
				if(currentIndex % 5 !=4)
				{
					Swap(&nNumbers[currentIndex], &nNumbers[currentIndex + 1]);
				}
				break;
			case KEY_UP:
				if(currentIndex / 5 != 0)
				{
					Swap(&nNumbers[currentIndex], &nNumbers[currentIndex - 5]);
				}
				break;
			case KEY_DOWN:
				if(currentIndex / 5 != 4)
				{
					Swap(&nNumbers[currentIndex], &nNumbers[currentIndex + 5]);
				}
				break;
		}
	}
}
