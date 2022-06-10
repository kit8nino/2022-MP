#include <iostream>
#include <cmath>
using namespace std;

double eps(double x, double y)
{
	return abs(y - x);
}
double f(double a)
{
	return (2 - a) * exp(a);
}
double c_func(double y, double x)
{
	return (x + y) / 2;
}

double dihotomia(double epsilon, double& x, double& y)
{
	double c;
	if (f(x) * f(y) < 0)
	{
		if (eps(y, x) > epsilon)
		{
			if (f(y) * f(c_func(y, x)) < 0)
			{
				x = c_func(y, x);
				c = x;
				dihotomia(epsilon, x, y);
			}
			else
				y = c_func(y, x);
			c = y;
			dihotomia(epsilon, x, y);
		}
		else return ((x + y) / 2);
	}
	return((x + y) / 2);
}

int main()
{
	double epsilon;
	cout << "Please, enter epsilon: ";
	cin >> epsilon;
	double a = -100;
	double b = 100;

	cout << dihotomia(epsilon, a, b) << endl;
}