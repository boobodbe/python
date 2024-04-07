# include <stdio.h>

// 求最大公因数
int gcd(int x, int y){return y ? gcd(y, x%y) : x;}

int main(){
	int num = gcd(12, 18);
	printf("%d\n", num);
	printf("试着用git编译一下c源文件试试可行不。\n");
}