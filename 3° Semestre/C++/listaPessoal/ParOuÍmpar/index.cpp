#include <iostream>
#include <string>

using namespace std;

string parImpar(int numero){
	if (numero%2 == 0){
		return "Par";
	} else {
		return "Ímpar";
	}
}

int main (){
	setlocale (LC_ALL, "portuguese");
	int numero;
	
	cout << "Programa Par ou Ímpar!" << endl;
	cout << "Digite o número: ";
	cin >> numero;
	
	cout << "O número é: " << parImpar(numero) << endl;
	
	return 0;
}
