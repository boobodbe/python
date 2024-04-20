# include <stdio.h>
# include <stdlib.h>
# include <string.h>

int yezhizhen(){
	// 野指针，free之后没设置成NULL，之后的指针分配的时候就会占用这个指针
	int *p1, *p2, *p3;
	p1 = (int *)malloc(4);
	*p1 = 1;
	p2 = (int *)malloc(4);
	*p2 = 2;
	free(p1);
	p1 = NULL;
	p3 = (int *)malloc(4);
	*p3 = 3;
	printf("*p3 = %d\n", *p3);
	*p1 = 100;
	printf("*p3 = %d\n", *p3);
	return 0;

}
int main(int argc, char const *argv[])
{
	// 指针与动态内存申请
	int n;  // 使用多少字节空间
	char* p;
	scanf("%d", &n); // 读取少申请空间的大小
	p = (char*)malloc(n);
	strcpy(p, "hello");
	puts(p);
	free(p); // p不能偏移，必须是最初的malloc返回的……值
	p = NULL; // 防止出现野指针
	yezhizhen(); 
	return 0;
}