#include <iostream>


using namespace std;

int lerNumero(){
	int a, b, c;
	cout << "Digite o Primeiro n�mero: "<< endl;
	cin >> a;
	cout << "Digite o Segundo n�mero: "<< endl;
	cin >> b;
	cout << "Digite o Terceiro n�mero: "<< endl;
	cin >> c;
	return a+b+c;
}

float media (int soma){
	return soma/3;
}

int main (){
	setlocale (LC_ALL, "portuguese");
	cout << "Programa Calcula M�dia!"<< endl;
	cout << "A m�dia �: " <<media(lerNumero()) << endl;
	return 0;
}
