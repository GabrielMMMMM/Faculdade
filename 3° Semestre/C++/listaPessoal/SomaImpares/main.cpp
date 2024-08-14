#include <iostream>

using namespace std;


int somaImpares(){
	int soma;
	
	for (int i = 0; i <= 100; i++){
		if(i%2 != 0){
			soma += i;
		}
	}
	
	return soma;
}

int main(){
	setlocale (LC_ALL, "portuguese");
	cout << "Soma de números ímpares de 1 a 100." << endl;
	
	cout<< "Resposta: " <<  somaImpares()<< endl;
	return 0;
}
