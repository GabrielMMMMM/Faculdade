#include <iostream>
#include <math.h>

using namespace std;

int main () {
	setlocale(LC_ALL, "portuguese");
	int a, b;
	cout << "Digite o valor de A: ";
	cin >> a;
	cout << "Digite o valor de B: ";
	cin >> b;
	int c = (a-b)*(a-b);
	cout << "O quadrado da diferença de A e B é igual a: " << c << endl;
	system ("pause");
}
