#include <iostream>
#include <string>

using namespace std;

string parImpar(int numero){
	if (numero%2 == 0){
		return "Par";
	} else {
		return "�mpar";
	}
}

int main (){
	setlocale (LC_ALL, "portuguese");
	int numero;
	
	cout << "Programa Par ou �mpar!" << endl;
	cout << "Digite o n�mero: ";
	cin >> numero;
	
	cout << "O n�mero �: " << parImpar(numero) << endl;
	
	return 0;
}
