#include <iostream>

using namespace std;

int fatorial (int numero){
	int fatorial =1;
	for (int i = numero ; i > 0; i--){
		fatorial *= i;
	}
	return fatorial;
}

int main (){
	setlocale (LC_ALL, "portuguese");
	int numero;
	do {
	
	cout << "Digite um número maior que 0: ";
	cin >> numero;
	} while (numero <= 0);
	
	cout << "O fatorial de " << numero << " é: " << fatorial(numero) << endl;
	
	return 0;
}
