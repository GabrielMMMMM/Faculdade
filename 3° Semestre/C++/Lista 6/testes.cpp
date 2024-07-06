#include <iostream>


using namespace std;


int encontrarMaior(int* vetor, int tamanho) {
    int maior = vetor[0]; // Inicializa o maior com o primeiro elemento do vetor
    for (int i = 1; i < tamanho; i++) { // Come�a a partir do segundo elemento
        if (vetor[i] > maior) { // Compara o elemento atual com o maior
            maior = vetor[i]; // Atualiza o maior, se necess�rio
        }
    }
    return maior;
}



int main () {
	
	setlocale(LC_ALL, "portuguese");
	int tamanho;
	
	cout << "Digite o tamanho do vetor: " << endl;
	cin >> tamanho;
	
	int vetor[tamanho];
	
	
	cout << "Digite "<<tamanho << " n�meros: " << endl;
	for (int i = 0; i < tamanho; i++){
		cin >> vetor [i];
		
	}
	
	cout << "O maior n�mero digitado �: " << encontrarMaior (vetor, tamanho);
	
	
	return 0;
	
		
}
