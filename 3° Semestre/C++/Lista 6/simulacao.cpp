#include "iostream"
#include "cstdlib"
using namespace std;
int main () { 
	setlocale(LC_ALL, "Portuguese");
	int aux = 10; // cria uma vari�vel inteira
	int *ptaux; // cria um ponteiro inteiro
	ptaux = &aux; // inicializa o ponteiro 
	cout<< "\nO valor de aux �:"<< aux;
	cout<< "\nO endere�o de mem�ria de aux � :"<< &aux;
	cout<< "\nO endere�o de mem�ria de aux � :"<< ptaux;
	cout<< "\nO endere�o de mem�ria ptaux �:" << &ptaux;
	cout<< "\nO valor de aux �:" << *ptaux;
	system("pause"); 
	return 0;
 }
