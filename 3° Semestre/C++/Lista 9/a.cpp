#include <iostream>

using namespace std;

int main(){
	int pedro = 2;
	int *corno = &pedro;
	
	cout << pedro << " Local da Memoria: " << corno;

	
	return 0;
}
