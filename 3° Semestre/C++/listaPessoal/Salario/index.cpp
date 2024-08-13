#include <iostream>


using namespace std;

float calculoSalario(float hora, int semana){
	float valorDia = hora*4;
	int mes = semana*4;
	
	return mes*valorDia;
}
int main(){
	setlocale(LC_ALL, "portuguese");
	int dia;
	float hora;
	
	cout << "Programa Calcula Salário!"<< endl;
	cout << "Digite o valor da hora(4hrs a aula): "<< endl;
	cin >> hora;
	cout << "Digite quantas aulas por semana(4 semanas no mês): "<< endl;
	cin >> dia;
	
	cout << "O seu Salário vai ser de: R$" << calculoSalario(hora, dia) << "." << endl;
	
	return 0;
	
}

