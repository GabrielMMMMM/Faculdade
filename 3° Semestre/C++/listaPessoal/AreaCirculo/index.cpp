#include <iostream>
#include <math.h>

using namespace std;

float calculaArea(float raio){
	float const pi = 3.14;
	float area = pi * pow(raio, 2);
	return area;
}


int main (){
	setlocale (LC_ALL, "portuguese");
	float raio;
	
	cout << "Programa Calcula �rea: " << endl;
	cout << "Digite o Raio da c�rculo: " ;	
	cin >> raio;
	
	cout << "A �rea �: " << calculaArea(raio) << endl;
	return 0;
}
