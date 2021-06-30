#include <iostream>
using namespace std;

struct product {
	int weight;
	int value;
};

int main() {
	int n;
	int w, v;
	cin >> n;
	product* plist = new product();

	for (int i = 0; i < n; i++) {
		cin >> w >> v;
		plist[i].weight = w;
		plist[i].value = v;
	}
	 
}