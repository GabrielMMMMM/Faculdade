#include <iostream>
#include <iomanip>

using namespace std;

float celsiusFahrenheit(int grau){
	float fahrenheit = grau * 9.0/5 + 32; 

	return fahrenheit;
}


int main(){
	setlocale(LC_ALL, "portuguese");
	float celsius;
	cout << "Digite quantos os Graus Celsius: " << endl;
	cin >> celsius;
	cout << fixed << setprecision(2);
	cout << celsius << " = " << celsiusFahrenheit(celsius) << endl;
	system ("pause");
	return 0;
}
