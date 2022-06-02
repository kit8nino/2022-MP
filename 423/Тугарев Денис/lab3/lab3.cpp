#include <iostream>
#include <math.h>
using namespace std;

double func(double x) {                             //Функция корни которой нам нужны
    return log10(1+2*x) - 2 + x;
}

double find_root (double a, double b, double e) // a и b абсциссы концов хорды , e - "эпсилон", необходимая точность
{
    while (fabs (b-a) > e) 
        {
         a = b - (b - a) * func(b) / (func(b) - func(a)); // в начале у нас a стоящая слева от знака равно это новое значение а, справа, заданное изначально, то есть a слева это x(i+1), а справа это x(i-1), в начальный момент x0 b это x(i)         
         b = a - (a - b) * func(a) / (func(a) - func(b));
        }
    return b;
} 
// a и b (i-1)-ый и i-ый члены

int main () 
{   
    double e; //Эпсилон, необходимая точность
    double x; //Корень уравнения
    cout << "Write epsilon = "; 
    cin >> e;
    x = find_root (0, 100, e); // т.к. промежуток по заданию у пользователя не спрашивается, то был выбран от 0 до 100(изначальные начало и конец хорды)
    cout << "Root: " << x << endl;
    return 0;
}