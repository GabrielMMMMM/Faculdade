#include <iostream>
#include <string>
#include <vector>

using namespace std;

//variaveis goblais
vector<string> nomes;
vector<int> idades;
vector<float> salarios;



string lerNome (){
	string nome;
	cout << "Digite seu nome: ";
	cin >> nome;
	return nome;
}

int lerIdade  (){
	int idade;
	cout << "Digite sua idade: ";
	cin >> idade;
	return idade;
}

float lerSalario(){
	float salario;
	cout << "Digite o seu salário: ";
	cin >> salario;
	return salario;
}

void guardarDados (string nome, int idade, float salario) {
	nomes.push_back(nome);
	idades.push_back(idade);
	salarios.push_back(salario);
}

	void listarDados (){
		for (int i = 0;  i < nomes.size(); i++){
			cout << nomes[i] << " - " << idades[i] << " - " << salarios[i] << endl;
		}
	}
	
	int main (){
		setlocale(LC_ALL, "portuguese");
		cout << "Dados Iniciais: " << endl;
		
		string nome_ = lerNome();
		int idade_ = lerIdade();
		float salario_ = lerSalario();
		guardarDados(nome_, idade_, salario_);
		int tecla;
		
		do{
			system("cls");
			cout << "Menu: \nAdd Dados. (Digite 1) \nExibir Dados (Digite 2)\nSair (Digite 3) \nOpção: ";
			cin >> tecla;
			
			switch (tecla){
				case 1: 
					system("cls");
					nome_ = lerNome();
					idade_ = lerIdade();
					salario_ = lerSalario();
					guardarDados(nome_, idade_, salario_);
					system("pause");
				break;
				case 2:
					system("cls");
					listarDados();
					system("pause");
				break;
				case 3:
					exit(0);
				break;
				default:
					cout <<"Opção errada!"<<endl;				
			}
			} while (tecla != 3);
		return 0;
}
