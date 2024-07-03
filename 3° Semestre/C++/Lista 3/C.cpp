#include <iostream>

using namespace std;

int main() {
    int A[20], B[20], C[20];

    // Ler as matrizes A e B do tipo vetor com 20 elementos
    for (int i = 0; i < 20; ++i) {
        cout << "Digite o elemento " << i + 1 << " de A: ";
        cin >> A[i];
    }

    for (int i = 0; i < 20; ++i) {
        cout << "Digite o elemento " << i + 1 << " de B: ";
        cin >> B[i];
    }

    // Construir a matriz C
    for (int i = 0; i < 20; ++i) {
        C[i] = A[i] - B[i];
    }

    // Apresentar a matriz C
    cout << "Matriz C:" << endl;
    for (int i = 0; i < 20; ++i) {
        cout << C[i] << " ";
    }

    return 0;
}
N
