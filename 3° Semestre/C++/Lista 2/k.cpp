#include <iostream>
#include <math.h>

using namespace std;

int main () {
	setlocale(LC_ALL, "portuguese");
	double cotacao, dolar, reais;
	cout << "Programa pra converter real em d�lar!\n";
	cout << "Digite o valor da Cota��o do d�lar: ";
	cin >> cotacao;
	cout << "Digite Quantos reais voc� tem: ";
	cin >> reais;
	
	dolar = reais / cotacao;
	cout << "Voc� tem: " << dolar << " d�lares!" << endl;
	system ("pause");
}
	
