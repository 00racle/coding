#include <iostream>

using namespace std;

struct student
{
	private:
		int id;
		const char *name;
		float percentage;
	public:
		void Show();
		void SetInfo(int _id, const char *_name, float _percentage);
};

void student::Show()
{
	cout<<"아이디: "<<id<<endl;
	cout<<"이름: "<<name<<endl;
	cout<<"백분률: "<<percentage<<endl;
}

void student::SetInfo(int _id, const char *_name, float _percentage)
{
	id = _id;
	name = _name;
	percentage = _percentage;
}

int main(void)
{
	student s;

	s.SetInfo(1, "김철수", 90.5);
	s.Show();
	return 0;
=======
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
