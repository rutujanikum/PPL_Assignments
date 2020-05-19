#include <stdio.h>
int facto(int);
int main() {
	int num = 3;
	int res = facto(3);
	return 0;
}
int facto(int num) {
	if(num == 1 || num == 0)
		return 1;
	else
		return num * facto(num-1);	
}
