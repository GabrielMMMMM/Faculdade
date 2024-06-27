#include <iostream>


using namespace std;

int main () {
	setlocale(LC_ALL, "portuguese");
	int a, b, c;
	cout << "Digite o valor A: ";
	cin >> a;
	cout << "Digite o valor B: ";
	cin >> b;
	cout << "Digite o valor C: ";
	cin >> c;		
	
	int d = (a*a) + (b*b) + (c*c);
	cout << "A soma dos quadrados de A, B e C é: " << d << endl;
	system ("pause");
}
