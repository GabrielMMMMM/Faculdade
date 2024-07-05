#include <iostream>

using namespace std;

// Definição da estrutura para representar os dados do trabalhador
struct Trabalhador {
    float salarioMensal;
    float percentualReajuste;
};

int main() {
    Trabalhador trabalhador;
    float novoSalario;

    // Leitura dos valores
    cout << "Digite o salário mensal do trabalhador: ";
    cin >> trabalhador.salarioMensal;
    cout << "Digite o percentual de reajuste a ser atribuído: ";
    cin >> trabalhador.percentualReajuste;

    // Calcula o novo salário
    novoSalario = trabalhador.salarioMensal * (1 + (trabalhador.percentualReajuste / 100));

    // Exibe o novo salário
    cout << "O novo salário do trabalhador é: " << novoSalario << endl;

    return 0;
}

