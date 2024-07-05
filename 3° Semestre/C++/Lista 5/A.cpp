#include <iostream>

using namespace std;

// Definição da estrutura para armazenar os valores
struct Valores {
    int A;
    int B;
    int C;
    int D;
};

int main() {
    Valores valores;
    int produto1, produto2, soma;

    // Leitura dos valores
    cout << "Digite o valor de A: ";
    cin >> valores.A;
    cout << "Digite o valor de B: ";
    cin >> valores.B;
    cout << "Digite o valor de C: ";
    cin >> valores.C;
    cout << "Digite o valor de D: ";
    cin >> valores.D;

    // Calcula os produtos e a soma
    produto1 = valores.A * valores.C;
    produto2 = valores.B * valores.D;
    soma = valores.B + valores.D;

    // Exibe os resultados
    cout << "O produto de A por C é: " << produto1 << endl;
    cout << "O produto de B por D é: " << produto2 << endl;
    cout << "A soma de B com D é: " << soma << endl;

    return 0;
}

