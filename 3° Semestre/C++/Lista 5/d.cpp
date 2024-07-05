#include <iostream>
#include <string>

using namespace std;


struct Pessoa {
    string nome;
    int idade;
};

int main (){

Pessoa pessoa1; // Declaração de uma variável do tipo Pessoa

cin >>  pessoa1.nome;
cout << pessoa1.nome;
}
