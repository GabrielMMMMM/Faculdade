#include <iostream>
#include <math.h>

using namespace std;

void notas(float saque){
	
	int moeda1, nota2, nota5, nota10, nota20, nota50, nota100;
	float moeda50, moeda25, moeda10, moeda5;
	
	if (saque/ 100 >= 1){
		nota100 = abs(saque / 100);
		saque -= (100 * nota100); 
		cout << "Notas de 100: " << nota100 << endl;
	} 
	if(saque/ 50 >= 1){
		nota50 = saque/50;
		saque -= (50 * nota50); 
		cout << "Notas de 50: " << nota50 << endl;
	} 
	if(saque/20 >= 1){
		nota20 = abs(saque / 20); 
		saque -= (20 * nota20); 
		cout << "Notas de 20: " << nota20 << endl;
		
	} 
	if(saque/10 >= 1){
		nota10 = abs(saque / 10); 
		saque -= (10 * nota10); 
		cout << "Notas de 10: " << nota10 << endl;
		
	}  
	if(saque/5 >= 1){
		nota5 = abs(saque / 5); 
		saque -= (5 * nota5); 
		cout << "Notas de 5: " << nota5 << endl;
	} 
	
	if(saque/2 >= 1){
		nota2 = abs(saque / 2); 
		saque -= (2 * nota2); 
		cout << "Notas de 2: " << nota2 << endl;
	}
	if (saque/ 1 >= 1){
		moeda1 = abs(saque / 1);
		saque -= (1 * moeda1); 
		cout << "Moedas de 1: " << moeda1 << endl;
	} 
	if (saque/ 0.5 >= 1){
		moeda50 = abs(saque / 0.5);
		saque -= (0.5 * moeda50); 
		cout << "Moedas de 50: " << moeda50 << endl;
	}
	if (saque/ 0.25 >= 1){
		moeda25 = abs(saque / 0.25);
		saque -= (0.25 * moeda25); 
		cout << "Moedas de 25: " << moeda25 << endl;
	}
	if (saque/ 0.1 >= 1){
		moeda10 = abs(saque / 0.1);
		saque -= (0.1 * moeda10); 
		cout << "Moedas de 10: " << moeda10 << endl;
	}
	if (saque/ 0.05 >= 1){
		moeda5 = abs(saque / 0.05);
		saque -= (0.05 * moeda5); 
		cout << "Moedas de 5: " << moeda5 << endl;
	}	
}

int main (){
	setlocale(LC_ALL, "portuguese");
	float saque; 
	cout << "Digite o valor do saque: ";
	cin >> saque;
	
	notas(saque);
	
	
	return 0;
}
