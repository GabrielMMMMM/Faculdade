#include <iostream>

using namespace std;

int main(){
	int n1 = 10;
	
	
	for (int i = 1, j = n1; j > 0; i++, j--){
		cout << i << " X " << j << " = " <<i * j << endl;
	}
	
	return 0;
}
