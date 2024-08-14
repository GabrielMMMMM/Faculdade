#include <iostream>

using namespace std;

int somaPares(){
	int numero = 100;
	int soma = 0;
	for (int i = 0; i <=100; i++){
		if (i%2 == 0){
			soma += i;
		}
	}
	return soma;
}

int main (){
	setlocale (LC_ALL, "portuguese");
	cout<< "A soma de todos os números pares de 0 a 100 é: " << somaPares()<< endl;
	return 0;
}
