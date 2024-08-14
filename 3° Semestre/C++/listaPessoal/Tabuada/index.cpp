#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){
	int colunas =1;
	
	cout << "TABUADA" << endl << endl;
	cout << "  ";
	while (colunas <= 10){
		cout.width(3);
		cout << colunas << " ";
		colunas ++;
	}
	cout << endl;
	 
	int linhas = 1;
	while (linhas <= 10){
		cout << linhas << "-";
		colunas =1;
		while (colunas <= 10){
			cout.width(3);
			cout << linhas * colunas << " ";
			colunas ++; 
		}
		linhas++;
		cout << endl;
		
	} 
	
	system ("pause");
	return 0;

}
