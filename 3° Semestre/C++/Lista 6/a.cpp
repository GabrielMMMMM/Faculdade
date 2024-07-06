#include <iostream>

using namespace std;

int main (){
	int a = 2, b = 1;
	int *pta = &a;
	int *ptb = &b;
	
	int soma = *pta + *ptb;
	
	cout << soma;
	
	return 0;
}

