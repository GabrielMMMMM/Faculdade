#include <iostream>


using namespace std;

int lerNumero(){
	int a, b, c;
	cout << "Digite o Primeiro número: "<< endl;
	cin >> a;
	cout << "Digite o Segundo número: "<< endl;
	cin >> b;
	cout << "Digite o Terceiro número: "<< endl;
	cin >> c;
	return a+b+c;
}

float media (int soma){
	return soma/3;
}

int main (){
	setlocale (LC_ALL, "portuguese");
	cout << "Programa Calcula Média!"<< endl;
	cout << "A média é: " <<media(lerNumero()) << endl;
	return 0;
}
