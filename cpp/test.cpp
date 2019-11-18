#include <iostream>

int main(void)
{
	for(int i=2; i<10; i++)
	{
		for(int j=1; j<10; j++)
		{
			std::cout<<i<<"x"<<j<<"="<<i*j<<std::endl;
		}
		std::cout<<std::endl;
	}
	return 0;
}
