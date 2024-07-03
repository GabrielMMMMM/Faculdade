#include <iostream>

using namespace std;

int main(){
	int vetor [10];
	for (int i=0; i<10; i++){
		cout << "Digite o valor do " << i+1 << "° do vetor. \n";
		cin >> vetor [i];
	}
	cout << "Vetor: " << "[";
	for (int i=0; i<10; i++){
		
		cout << vetor [i] << ", ";
	}
	cout << "]" << endl;
	system ("pause");
}
