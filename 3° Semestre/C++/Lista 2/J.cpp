#include <iostream>
#include <math.h>

using namespace std;

int main () {
	setlocale(LC_ALL, "portuguese");
	double cotacao, dolar, reais;
	cout << "Programa pra converter dólar em real!\n";
	cout << "Digite o valor da Cotação do dólar: ";
	cin >> cotacao;
	cout << "Digite Quantos dólares você tem: ";
	cin >> dolar;
	
	reais = dolar * cotacao;
	cout << "Você tem: " << reais << " reais!" << endl;
	system ("pause");
	
	
}
