#include <iostream>
#include <math.h>

using namespace std;

int main () {
	setlocale(LC_ALL, "portuguese");
	double cotacao, dolar, reais;
	cout << "Programa pra converter d�lar em real!\n";
	cout << "Digite o valor da Cota��o do d�lar: ";
	cin >> cotacao;
	cout << "Digite Quantos d�lares voc� tem: ";
	cin >> dolar;
	
	reais = dolar * cotacao;
	cout << "Voc� tem: " << reais << " reais!" << endl;
	system ("pause");
	
	
}
