#include <iostream>
#include <vector>
using namespace std;

int main (){
	setlocale(LC_ALL,"portuguese");
	
	vector<int> serie;
    serie.push_back(0);
    serie.push_back(1);
    
	int resultado;
	
	cout << "Série Fibonacci: " << endl;
	cout << serie[0] << endl; 
	
	for (int i = 0; i < 99; i++){
		resultado = serie[i] + serie [i+1];
		serie.push_back(resultado); 
		cout << serie[i+1]<< endl;	
	}
	



	return 0;
}
