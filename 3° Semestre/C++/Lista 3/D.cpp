#include <iostream>

using namespace std;

int main() {
    int A[15], B[15];

    // Ler 15 elementos de uma matriz tipo vetor
    for (int i = 0;  i < 15; ++i) {
        cout << "Digite o elemento " << i + 1 << " de A: ";
        cin >> A[i];
    }

    // Construir a matriz B com o quadrado dos elementos de A
    for (int i = 0; i < 15; ++i) {
        B[i] = A[i] * A[i];
    }

    // Apresentar as matrizes A e B
    cout << "Matriz A:";
    for (int i = 0; i < 15; ++i) {
        cout << " " << A[i];
    }
    cout << endl;

    cout << "Matriz B:";
    for (int i = 0; i < 15; ++i) {
        cout << " " << B[i];
    }

    return 0;
}

