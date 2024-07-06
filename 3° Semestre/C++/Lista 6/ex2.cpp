#include <iostream>
#include <cstdlib>
#include <string>
#define n 2

using namespace std;

//struct inicial
typedef struct meuCadastro cadastro;

struct meuCadastro {
	string nome[n];
	int idade [n];
	char sexo [n];
	float salario [n];
	float novoSalario [n];	
};

//variaveis globais
cadastro tb;
cadastro *ptb = &tb;
int linha = -1;

//funcoes
string lerNome (){
	string nome;
	cout << "Digite o Nome: ";
	cin >> nome;
	return nome;
	
}

int lerIdade (){
	int idade;
	cout << "Digite a Idade: ";
	cin >> idade;
	return idade;
}

char lerSexo (){
	//colocar alguma coisa pra fazer o cin sempre ler maiuscula
	char sexo;
	do {
		cout << "Digite o sexo (M/F)";
		cin >> sexo;
	} while (sexo != 'M' && sexo != 'F');
	return sexo;
}

float lerSalario (){
	float salario;
	cout << "Digite o salário: ";
	cin >> salario;
	return salario;
}

float aumentoSalario(float *salario){
	float novoSalario;
	novoSalario = *salario + (*salario *0.10);
	return novoSalario;
}


void novaLinhaStruct (){
	if ( linha == n-1 ) return;
	linha ++;
	ptb -> nome [linha] = lerNome();
	ptb -> idade [linha] = lerIdade();
	ptb -> sexo [linha] = lerSexo();
	ptb -> salario [linha] = lerSalario();
	ptb -> salario [linha] = aumentoSalario(&ptb -> salario [linha]);
}

void listarLinhasStruct (){
	cout << "Dados: " << endl;
	for (int i = 0; i <= linha; i++){
		cout << "Nome: " << ptb -> nome [i]<< endl;
		cout << "Idade: " << ptb -> idade [i]<< endl;
		cout << "Sexo: " << ptb -> sexo [i]<< endl;
		cout << "Salário: R$" << ptb -> salario [i]<< endl;
		cout << "Novo Salário: R$" << ptb -> novoSalario [i]<< endl;
		
		
	}
}


int main (){
	setlocale (LC_ALL, "portuguese");
	int tecla;
	do{
		system("cls");
		cout << "Ler Dados (Digite 1) \nExibir Dados (Digite 2) \nSair (Digite 3)"<< endl;
		cin >> tecla;
		switch (tecla){
			case 1:
				system ("cls");
				novaLinhaStruct ();
			break;
			case 2:
				system ("cls");
				if (linha == -1){
					cout << "Add itens Primeiro"<< endl;
					system ("pause");
				} else {
				listarLinhasStruct ();
				system ("pause");
				}
			break;
			case 3:
				system ("cls");
				exit (0);
			break;	
			default:
				system("cls");
				cout <<"Nenhuma das opção foi digitada! Tente novamente.";	
				system("pause");	
		}
	} while(tecla != 3);
	
	return 0;
}
