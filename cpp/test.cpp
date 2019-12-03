#include <iostream>
using namespace std;

#define ID_LEN		20
#define MAX_SPD		200
#define FUEL_STEP	2
#define ACC_STEP	10
#define BRK_STEP	10

struct Car
{
	char gmaerID[ID_LEN];		//소유자 ID
	int fuelGauge;				//연료량
	int curSpeed;				//현재속도
};

void ShowCarState(const Car &car)
