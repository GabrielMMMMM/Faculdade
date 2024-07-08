#include <iostream>
#include <cstdlib>
#include <stdlib.h>
 
using namespace std;
 
//criacao do struct
typedef struct Nopilha pilha;
struct Nopilha
{
	int valor;
	pilha *ant;
};
 
 
int cont; // para contar os nós
pilha *topo;
 
void construtor() {
	topo = NULL;
	cont = 0; }
 
bool push(int valor) {
	pilha *newpilha = (pilha*) malloc(sizeof(pilha));
	if (newpilha == NULL) return false;
	newpilha->valor = valor;
	newpilha->ant = topo;
	topo = newpilha;
	cont ++; // incrementa quantidade de nós
	return true;
}
 
bool pop ( ) { 
	int valor; 
	pilha *temp;
	temp = topo;
	valor = topo->valor;
	topo = topo->ant;
	free(temp);
	cout << "\nO valor removido foi:" << valor << endl;
	return true;
}
 
void exibirpilha ( ) {
	pilha *temp;
	temp= topo;
	while (temp->ant != NULL){
		cout << "\n" << temp->valor << endl;
		temp = temp->ant;
	}
	system("pause");
}
 
bool vazia() {
	if (topo == NULL ) return true;
	else return false;
}
 
void destrutor() { 
	pilha *temp;
	while (topo != NULL) {
		temp = topo;
		topo = topo->ant;
		free(temp);
		cont--; 
	}
	free(topo);
	cout << "\na pilha foi destruida!\n";
}
 
int total ( ) {
	pilha * temp;
	temp = topo;
	int cont = 0;
	while (temp != NULL ){ 
	cont ++;
	temp=temp->ant; 
	}
	return cont;
}
 
 
int main (){
	setlocale(LC_ALL, "portuguese");
	int n, valor;
	do{
		system ("cls");
		cout<<"1- Add valor \n2- Exibir Valores \n3- Apagar Valor \n4- Mostrar Quantidade \n5- Sair" << endl;
		cin >> n;
		switch (n){
			case 1:
				system ("cls");
				cout << "Digite um valor para continuar" << endl;
				cin >> valor;
				push(valor);
				system ("pause");
			break;
			case 2:
				system ("cls");
				cout << exibirpilha ( ) << endl;
				system ("pause");
			break;
			case 3:
				system ("cls");
				cout << destrutor() << endl;
				system ("pause");
			break;
			case 4:
				system ("cls");
				cout << "O valor total de pilhas é de: "<< total() << endl;
				system ("pause");
			break;
			case 5:
				exit(0);
			break;	
			default:
				system ("cls");
				cout << "Não tem essa opção!" << endl;
				system ("pause");
		}	
	} while(n != 5);
	return 0;
}
