#include <iostream>

using namespace std;

float soma(){
	float n1, n2;
	cout << "Digite o valor do primeiro n�mero: ";
	cin >> n1;
	cout << "Digite o valor do segundo n�mero: ";
	cin >> n2;
	return n1+n2;
}

float subtracao(){
	float n1, n2;
	cout << "Digite o valor do primeiro n�mero: ";
	cin >> n1;
	cout << "Digite o valor do segundo n�mero: ";
	cin >> n2;
	return n1 - n2;
	
}

float multiplicacao(){
	float n1, n2;
	cout << "Digite o valor do primeiro n�mero: ";
	cin >> n1;
	cout << "Digite o valor do segundo n�mero: ";
	cin >> n2;
	return n1*n2;	
	
}

float divisao(){
	float n1, n2;
	cout << "Digite o valor do primeiro n�mero: ";
	cin >> n1;
	cout << "Digite o valor do segundo n�mero: ";
	cin >> n2;
	return n1/n2;
}



int main (){
	setlocale (LC_ALL, "portuguese");
	int tecla;
	float resultado;
	do {
		system ("cls");
		cout << "CALCULADORA"<< endl << endl;
		cout << "1- Soma \n2- Subtra��o \n3- Multiplica��o \n4- Divis�o \n5- Sair" << endl << endl;
		cin >> tecla;
		switch (tecla){
			case 1:
				system("cls");
				resultado  = soma();
				cout << "Resultado: " << resultado  << endl << endl;
				system("pause");
				break;
			case 2:
				system("cls");
				resultado = subtracao();
				cout << "Resultado: " << resultado << endl << endl;
				system("pause");
				break;	
			case 3:
				system("cls");
				resultado = multiplicacao();
				cout << "Resultado: " << resultado  << endl << endl;
				system("pause");
				break;
			case 4:
				system("cls");
				resultado = divisao();
				cout << "Resultado: " << resultado << endl << endl;
				system("pause");
				break;
			case 5:
				exit (0);
				break;
			default:
				cout << "N�o tem essa op��o! Tente novamente." << endl;
				system ("pause");				
		} 
	}while (tecla != 5);
	
	return 0;
}
