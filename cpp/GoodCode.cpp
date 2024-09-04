# include <stdio.h>

// 求最大公因数
int gcd(int x, int y){return y ? gcd(y, x%y) : x;}

int add(int x, int y)
{
	return x + y;
}

int main(){
	int num = gcd(27, 18);
	printf("gcd(27, 18) = %d\n", num);
    printf("Hello World!\n");
	printf("add(3, 4) = %d\n", add(3, 4));
	return 0;
}