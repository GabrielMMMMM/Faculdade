#include <iostream>
#include <vector>
#include <cstdlib> // Para system("cls") e exit()
#include <limits> // Para usar numeric_limits
#include <iomanip> // Para usar setprecision
#include <algorithm> // Para usar std::min_element e std::max_element

using namespace std;

int main() {
    vector<int> valores;
    int entrada;
    int soma = 0;
    int maior, menor;
    float media;
    char tecla;

    do {
        system("cls"); // Limpa a tela no Windows
        cout << "Menu:\n";
        cout << "1. Adicionar número\n";
        cout << "2. Mostrar dados\n";
        cout << "3. Sair\n";
        cout << "Escolha uma opção: ";
        cin >> tecla;

        switch (tecla) {
            case '1':
                system("cls");
                cout << "Digite o número a ser adicionado: ";
                cin >> entrada;
                valores.push_back(entrada);
                cout << "Número adicionado com sucesso!\n";
                system("pause");
                break;
            case '2':
                system("cls");
                if (valores.empty()) {
                    cout << "Nenhum número foi adicionado.\n";
                } else {
                    soma = 0;
                    maior = *max_element(valores.begin(), valores.end());
                    menor = *min_element(valores.begin(), valores.end());
                   for (auto i = valores.begin(); i != valores.end(); i++) {
   						 soma += *i;
					}

                    media = static_cast<float>(soma) / valores.size();
                    cout << "Soma: " << soma << endl;
                    cout << "Média: " << fixed << setprecision(2) << media << endl;
                    cout << "Maior valor: " << maior << endl;
                    cout << "Menor valor: " << menor << endl;
                }
                system("pause");
                break;
            case '3':
                cout << "Saindo...\n";
                break;
            default:
                cout << "Opção inválida. Tente novamente.\n";
                system("pause");
                break;
        }
    } while (tecla != '3');

    return 0;
}

