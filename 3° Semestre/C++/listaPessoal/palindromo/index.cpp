#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool verificaPalindromo(string palavra){
	//remover espacos
	palavra.erase(remove(palavra.begin(), palavra.end(), ' '), palavra.end());	
	string verifica = "";
	
	for (int i =palavra.length() - 1; i >= 0; i--){
		verifica += palavra[i];
		
	}
	if (palavra == verifica){
		return true;
	} else {
		return false;
	}
}

int main(){
	setlocale(LC_ALL, "portuguese");
	string palavra;
	cout << "Digite uma palavra: " << endl;
	cin >> palavra;
	if (verificaPalindromo(palavra)){
		cout << "É um palindromo!";
	} else {
		cout << "Não é um palindromo!";
	}
	
	return 0;
}
