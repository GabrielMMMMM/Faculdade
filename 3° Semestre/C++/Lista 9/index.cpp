#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definição da estrutura para armazenar dados de uma pessoa
typedef struct Pessoa {
    char nome[50];
    float salario;
    struct Pessoa *prox;
} Pessoa;

// Função para criar um novo nó na pilha
Pessoa* criarPessoa(char nome[], float salario) {
    Pessoa *novaPessoa = (Pessoa*)malloc(sizeof(Pessoa));
    if (novaPessoa == NULL) {
        printf("Erro ao alocar memória.\n");
        exit(1);
    }
    strcpy(novaPessoa->nome, nome);
    novaPessoa->salario = salario;
    novaPessoa->prox = NULL;
    return novaPessoa;
}

// Função para empilhar uma pessoa na pilha
void empilhar(Pessoa **topo, char nome[], float salario) {
    Pessoa *nova = criarPessoa(nome, salario);
    nova->prox = *topo;
    *topo = nova;
    printf("Pessoa empilhada com sucesso!\n");
}

// Função para desempilhar uma pessoa da pilha
void desempilhar(Pessoa **topo) {
    if (*topo == NULL) {
        printf("A pilha está vazia.\n");
        return;
    }
    Pessoa *temp = *topo;
    *topo = (*topo)->prox;
    printf("Pessoa desempilhada: %s\n", temp->nome);
    free(temp);
}

// Função para exibir todas as pessoas empilhadas
void exibirPilha(Pessoa *topo) {
    if (topo == NULL) {
        printf("A pilha está vazia.\n");
        return;
    }
    printf("Pessoas empilhadas:\n");
    while (topo != NULL) {
        printf("Nome: %s, Salário: %.2f\n", topo->nome, topo->salario);
        topo = topo->prox;
    }
}

int main() {
    Pessoa *topo = NULL;
    int opcao;
    char nome[50];
    float salario;

    do {
        printf("\nMenu:\n");
        printf("1. Adicionar pessoa\n");
        printf("2. Remover pessoa\n");
        printf("3. Exibir todas as pessoas\n");
        printf("4. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite o nome da pessoa: ");
                scanf("%s", nome);
                printf("Digite o salário da pessoa: ");
                scanf("%f", &salario);
                empilhar(&topo, nome, salario);
                break;
            case 2:
                desempilhar(&topo);
                break;
            case 3:
                exibirPilha(topo);
                break;
            case 4:
                printf("Saindo...\n");
                break;
            default:
                printf("Opção inválida. Tente novamente.\n");
        }
    } while (opcao != 4);

    // Liberar a memória da pilha antes de sair do programa
    while (topo != NULL) {
        Pessoa *temp = topo;
        topo = topo->prox;
        free(temp);
    }

    return 0;
}

