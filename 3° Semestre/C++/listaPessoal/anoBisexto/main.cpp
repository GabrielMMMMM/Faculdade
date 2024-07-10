#include <iostream>

using namespace std;


bool bisexto (int ano){
	if (ano % 4 == 0 ){
		return true;
	}
	return false;
}
int main(){
	setlocale (LC_ALL, "portuguese");
	int ano;
	cout << "Programa Verifica Ano Bisexto!" << endl;
	cout << "Digite o ano: ";
	cin >> ano;
	
	if (bisexto(ano)){
		if (ano <= 2024){
			cout << ano << " foi um ano bisexto!";
		} else {
			cout << ano << " será um ano bisexto!";
		}	 
	} else {
		cout << ano << " não foi um ano bisexto!";
	}
	
	return 0;
}
