#include <iostream>

using namespace std;

bool numeroPrimo(int numero){
	if (numero <= 1){
		return false;
	}
	for(int i = 2; i * i <= numero; i++){
		
		if (numero%i == 0){
			return false;
		}
		
	} 
		return true;
	
}

int main(){
	setlocale(LC_ALL, "portuguese");
	int numero;
	cout << "Digite um número: " << endl;
	cin >> numero;
	if (numeroPrimo(numero)){
		cout << "É primo" << endl;
		
	} else {
		cout << "Não é primo" << endl;
	}
	return 0;
}
