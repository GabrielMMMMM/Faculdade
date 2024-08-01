#include <iostream>

using namespace std;

float soma(){
	float n1, n2;
	cout << "Digite o valor do primeiro número: ";
	cin >> n1;
	cout << "Digite o valor do segundo número: ";
	cin >> n2;
	return n1+n2;
}

float subtracao(){
	float n1, n2;
	cout << "Digite o valor do primeiro número: ";
	cin >> n1;
	cout << "Digite o valor do segundo número: ";
	cin >> n2;
	return n1 - n2;
	
}

float multiplicacao(){
	float n1, n2;
	cout << "Digite o valor do primeiro número: ";
	cin >> n1;
	cout << "Digite o valor do segundo número: ";
	cin >> n2;
	return n1*n2;	
	
}

float divisao(){
	float n1, n2;
	cout << "Digite o valor do primeiro número: ";
	cin >> n1;
	cout << "Digite o valor do segundo número: ";
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
		cout << "1- Soma \n2- Subtração \n3- Multiplicação \n4- Divisão \n5- Sair" << endl << endl;
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
				cout << "Não tem essa opção! Tente novamente." << endl;
				system ("pause");				
		} 
	}while (tecla != 5);
	
	return 0;
}
