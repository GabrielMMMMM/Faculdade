#include <iostream>

using namespace std;

int main (){
	int vetorA [8] = {1, 2, 3, 4, 5, 6, 7, 8};
	int vetorB [8];
	
	for (int i = 0; i < 8; i++){
		vetorB [i] = vetorA[i]*3;
		
	}
	for (int i = 0; i < 8; i++){
		cout << vetorB [i] << " ";
	}
	system ("pause");
	
}
