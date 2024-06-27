#include <iostream>

using namespace std;

int main (){
	setlocale(LC_ALL, "portuguese");
	int volume, altura, comprimento, largura;
	
	cout << "Programa pra calcular o Volume!\n";
	cout << "Digite a Altura: ";
	cin >> altura;
	cout << "Digite o Comprimento: ";
	cin >> comprimento;
	cout << "Digite a Largura: ";
	cin >> largura;
	
	volume = altura*largura*comprimento;
	cout << "O Volume é: " << volume << endl;
	system ("pause");
	
}
