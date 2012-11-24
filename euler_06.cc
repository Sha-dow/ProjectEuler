/*Laskee summien neliön ja neliöiden summan erotuksen*/

#include <cstdlib>
#include <iostream>

using namespace std;

int laske_erotus(int raja)
{
	int summien_nelio = 0;
	int nelioiden_summa = 0;
	int tulos = 0;
	
	for (int i = 0; i <= raja; i += 1)
	{
		summien_nelio = summien_nelio + i;
		nelioiden_summa = nelioiden_summa + (i*i);
	}
	
	summien_nelio = (summien_nelio * summien_nelio);
	tulos = summien_nelio - nelioiden_summa;
	
	return tulos;
}

int main()
{
	int raja = 0;
	
	cout << "Syötä raja: " << endl;
	cin >> raja;
	
	cout << "Tulos on: " << laske_erotus(raja) << endl;
	
	return EXIT_SUCCESS;	
}
