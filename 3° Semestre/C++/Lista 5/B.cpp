#include <iostream>

using namespace std;

// Defini��o da estrutura para representar os dados do trabalhador
struct Trabalhador {
    float salarioMensal;
    float percentualReajuste;
};

int main() {
    Trabalhador trabalhador;
    float novoSalario;

    // Leitura dos valores
    cout << "Digite o sal�rio mensal do trabalhador: ";
    cin >> trabalhador.salarioMensal;
    cout << "Digite o percentual de reajuste a ser atribu�do: ";
    cin >> trabalhador.percentualReajuste;

    // Calcula o novo sal�rio
    novoSalario = trabalhador.salarioMensal * (1 + (trabalhador.percentualReajuste / 100));

    // Exibe o novo sal�rio
    cout << "O novo sal�rio do trabalhador �: " << novoSalario << endl;

    return 0;
}

