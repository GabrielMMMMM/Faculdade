#include <iostream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

float calculoMulta (float divida) {
	float multa =  (divida * 0.02);
	return multa;
}

float calculoJuros (float divida, int tempo){
	float mes = tempo / 30;
	round(mes);
	float juros = (divida * mes * 0.01);
	return juros;
	
}

int main (){
	setlocale(LC_ALL, "portuguese");
	int tecla;
	float divida;
	int atraso;
	float total;
	cout << "Dados Iniciais: " << endl; 
	cout << "Digite o valor da Dívida: ";
	cin >> divida;
	cout << "Digite o tem em atraso(em dias): ";
	cin >> atraso;
	do{
		cout << "\nMENU:\n\nMostrar valor da dívida (digite 1).\nMotrar valor da multa(digite 2)\nMostrar valor do juros mensal(digite 3)\nMostrar o valor total a pagar(digite 4)\nSair(digite 5)\n\n\n";
		cin >> tecla;
		switch (tecla) {
			case 1: 
				system("cls");
				cout << "Valor da dívida:  " << endl;
				cout << "R$: " << divida << ".\n";
				system("pause");
			break;
			case 2: 
				system("cls");
				cout << "Valor da Multa: " << endl;
				cout << "R$: " << calculoMulta(divida) << ".\n";
				system("pause");
			break;
			case 3:
				system("cls");
				cout <<"Valor do Juros: " << endl;
				cout <<"R$: " << calculoJuros(divida, atraso) << ".\n"; 
				system("pause");
			break;
			case 4:
				system("cls");
				total = divida + calculoJuros(divida, atraso) + calculoMulta(divida); 
				cout << "Valor Total a Pagar: " << endl;
				cout << "R$: " << total << ".\n";
				system("pause");
			break;
			case 5:
				exit(0);
			break;	
			default:
				cout<< "Botão não reconhecido! Tente novamente.";	
		}
	} while (tecla != 5);
	return 0;
}
