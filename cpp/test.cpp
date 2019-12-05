#include <iostream>
using namespace std;

class Point{
	private:
		int x;
		int y;
	public:
		//디폴트 생성자
		Point(){
			x = 10;
			y = 15;
		}
		Point(int x, int y){
			this->x = x;
			this->y = y;
		}
		void print(){
			cout<<"X: "<<x<<", Y: "<<y<<"\n";
		}
};

int main(void){
	Point p;
	p.print();

	Point p2 = { 3, 4 };
	p2.print();
}
