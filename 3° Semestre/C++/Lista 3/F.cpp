#include <iostream>

using namespace std;

int main() {
    int A[20], B[30], C[50];

    // Ler duas matrizes do tipo vetor, A com 20 elementos e B com 30 elementos
    for (int i = 0; i < 20; ++i) {
        cout << "Digite o elemento " << i + 1 << " de A: ";
        cin >> A[i];
    }

    for (int i = 0; i < 30; ++i) {
        cout << "Digite o elemento " << i + 1 << " de B: ";
        cin >> B[i];
    }

    // Construir a matriz C, junção de A e B com capacidade para 50 elementos
    for (int i = 0; i < 50; ++i) {
        if (i < 20) {
            C[i] = A[i];
        } else {
            C[i] = B[i - 20];
        }
    }

    // Apresentar a matriz C
    cout << "Matriz C:" << endl;
    for (int i = 0; i < 50; ++i) {
        cout << C[i] << " ";
    }

    return 0;
}

