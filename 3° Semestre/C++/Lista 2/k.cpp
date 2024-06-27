#include <iostream>
#include <math.h>

using namespace std;

int main () {
	setlocale(LC_ALL, "portuguese");
	double cotacao, dolar, reais;
	cout << "Programa pra converter real em dólar!\n";
	cout << "Digite o valor da Cotação do dólar: ";
	cin >> cotacao;
	cout << "Digite Quantos reais você tem: ";
	cin >> reais;
	
	dolar = reais / cotacao;
	cout << "Você tem: " << dolar << " dólares!" << endl;
	system ("pause");
}
	
