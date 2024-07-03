#include <iostream>

using namespace std;

int main() {
    int A[20], B[20];

    // Ler 20 elementos de uma matriz A tipo vetor
    for (int i = 0; i < 20; ++i) {
        cout << "Digite o elemento " << i + 1 << " de A: ";
        cin >> A[i];
    }

    // Construir a matriz B com os elementos invertidos de A
    for (int i = 0; i < 20; ++i) {
        B[i] = A[19 - i];
    }

    // Apresentar as matrizes A e B lado a lado
    cout << "Matriz A | Matriz B:" << endl;
    for (int i = 0; i < 20; ++i) {
        cout << A[i] << "       | " << B[i] << endl;
    }

    return 0;
}

