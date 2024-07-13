#include <iostream>

using namespace std;


float calculoArea(float lado){
	return lado*lado;
}
int main(){
	setlocale(LC_ALL, "portuguese");
	float lado;
	cout << "Digite o lado do Quadrado: ";
	cin >> lado;
	
	cout << "A área do quadrado é: " << calculoArea(lado) << endl;
	
		
	return 0;
}
