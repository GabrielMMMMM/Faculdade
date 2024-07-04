#include <iostream>
#include <string>
#include <vector>

using namespace std;

//variaivais goblais
vector <int> idades;
vector <string> nomes;

string lerNome(){
	string nome_;
	cout << "Digite seu nome: ";
	cin >>  nome_;
	return nome_;
	
}
int lerIdade(){
	int idade_;
	cout << "Digite sua idade: ";
	cin >> idade_;
	return idade_;
}

void guardarDados (string nome, int idade){
	nomes.push_back(nome);
	idades.push_back(idade);
}
void listarDados (){
	for (int i = 0; i < nomes.size(); i++){
		cout << nomes[i] << " - " << idades[i] << endl;
	}
}

int saldoIdade(){
	int soma = 0;
	for (int i = 0; i < idades.size(); i++){
		soma += idades[i];
	}
	return soma;
}
float mediaIdade(int tamanho, float soma){
	float media = soma/tamanho;
	return media;
}
	
string maiorIdade(){
   int idadeMaior = idades[0];
    string nomeMaior = nomes[0];

    for (int i = 1; i < idades.size(); i++){
        if (idades[i] > idadeMaior){
            idadeMaior = idades[i];
            nomeMaior = nomes[i];
        }
    }
    return nomeMaior;
}

string menorIdade(){
	
    int idadeMenor = idades[0];
    string nomeMenor = nomes[0];

    for (int i = 1; i < idades.size(); i++){
        if (idades[i] < idadeMenor){
            idadeMenor = idades[i];
            nomeMenor = nomes[i];
        }
    }
    return nomeMenor;
}


int main(){
	setlocale(LC_ALL, "portuguese");
	int tecla;
	cout << "Dados Iniciais"<< endl;
	string nome = lerNome();
	int idade = lerIdade();
	guardarDados (nome, idade);
	cout << "Dados computados!" << endl;
	do {
		system("cls");
		cout << "\nMenu: \n\nAdicionar Dados (digite 1). \nMostra Pessoa com Maior Idade (digite 2) \nMostra Pessoa com Menor Idade (digite 3)\nMostra Média (digite 4) \nMostra Saldo (digite 5) \nListar Dados (digite 6)\nSair (digite 7) \n\nOpção: ";
		cin >> tecla;
		switch (tecla){
			case 1:
				system("cls");
				nome = lerNome();
				idade = lerIdade();
				guardarDados (nome, idade);
				cout << "Dados computados!" << endl;
				system("pause");
			break;
			case 2:
				system("cls");
				if (idades.size() < 2){
					cout << "Adicione mais dados para ter acesso a essa opção!" << endl;
				} else {
					cout << "Pessoa Com a Maior idade: " << endl;
					cout << maiorIdade() << endl;
				}
				system("pause");
				
			break;
			case 3:
				system("cls");
				if (idades.size() < 2){
					cout << "Adicione mais dados para ter acesso a essa opção!" << endl;
				} else {
					cout << "Pessoa Com a Menor idade: ";
					cout << menorIdade() << endl;
				}
				system("pause");
			break;	
			case 4:
				system("cls");
				cout << "Média das idades: ";
				cout << mediaIdade(idades.size(), saldoIdade()) << endl;
				system("pause");
			break;
			case 5:
				system("cls");
				cout << "Saldo idades: ";
				cout << saldoIdade() << endl;
				system("pause");
			break;	
			case 6:
				system("cls");
				cout << "Dados do Sistema: \n\n\n";
				listarDados() ;
				system("pause");
			break;	
			case 7:
				exit(0);
			break;	
			default:
				system("cls");
				cout <<"Nenhuma das opção foi digitada! Tente novamente.";	
				system("pause");
		}
	} while(tecla != 7);
	
	return 0;		
}

