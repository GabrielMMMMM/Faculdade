#include <iostream>

using namespace std;

int main() {
    int A[15], B[15], C[30];

    // Ler duas matrizes A e B do tipo vetor com 15 elementos cada
    for (int i = 0; i < 15; ++i) {
        cout << "Digite o elemento " << i + 1 << " de A: ";
        cin >> A[i];
    }

    for (int i = 0; i < 15; ++i) {
        cout << "Digite o elemento " << i + 1 << " de B: ";
        cin >> B[i];
    }

    // Construir a matriz C, junção de A e B
    for (int i = 0; i < 30; ++i) {
        if (i < 15) {
            C[i] = A[i];
        } else {
            C[i] = B[i - 15];
        }
    }

    // Apresentar a matriz C
    cout << "Matriz C:" << endl;
    for (int i = 0; i < 30; ++i) {
        cout << C[i] << " ";
    }

    return 0;
}

