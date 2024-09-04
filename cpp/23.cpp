// 顺序查找原理及实战, 折半查找原理及实战， 二叉排序树
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef int Elemtype;
// 顺序查找
typedef struct 
{
	Elemtype* elem; // 整型指针，申请的堆空间的起始地址存入elem
	int TableLen; // 存储动态数组里面元素的个数
}SSTable;

void ST_Init(SSTable &ST, int len)
{
	// 多申请一个位置，用来存哨兵
	ST.TableLen = len+1;
	ST.elem = (Elemtype*)malloc(sizeof(Elemtype)*ST.TableLen);
	srand(time(NULL)); // 随机数生成
	int i;
	for(i = 1; i<ST.TableLen; i++)
	{
		ST.elem[i] = rand()%100;
	}
}

void ST_print(SSTable ST)
{
	// 打印顺序表
	int i;
	for(i = 1; i<ST.TableLen; i++)
	{
		printf("%3d", ST.elem[i]);
	}
	printf("\n");
}

int Search_Seq(SSTable ST, Elemtype key)
{
	// 顺序查找
	ST.elem[0] = key; // 让零号位置作为哨兵
	int i;
	for(i = ST.TableLen -1; ST.elem[i] != key; --i);
	return i;
}

// 折半查找，又叫二分查找，它只适用于有序的顺序表
int BinarySearch(SSTable L, Elemtype key)
{
	int low = 0;
	int high = L.TableLen-1;
	int mid;
	while(low<=high)
	{
		mid = (low+high)/2;
		if(key>L.elem[mid])
		{
			low = mid +1;
		}else if(key<L.elem[mid])
		{
			high = mid - 1;
		}else{
			return mid;
		}
	}
	return -1;
}

int compare(const void *left, const void *right)
{
	// 函数名中存储的是函数的入口地址，也是一个指针，是函数指针类型
	// left和right指向数组的任意两个元素
	// qsort规定如果left指针指向的值大于right指针指向的值，返回正值，小于，返回负值，相等返回0
	return *(int *)left - *(int *)right; // 从小到大排序
	// return *(Elemtype *)right - *(Elemtype *)left; // 从大到小排序
}

int main()
{
	printf("Hello World!\n");
	printf("============SS============\n");
	SSTable ST;
	ST_Init(ST, 10);
	ST_print(ST);
	printf("please input search your key: ");
	Elemtype key;
	scanf("%d", &key);
	int pos;
	pos = Search_Seq(ST, key);
	if(pos)
	{
		printf("find key, pos is %d.\n", pos);
	}
	else
	{
		printf("not find.\n");
	}
	printf("\n===========binary search===========\n");
	SSTable BS;
	ST_Init(BS, 10);
	ST_print(BS);
	qsort(BS.elem, BS.TableLen, sizeof(Elemtype), compare); // 排序
	ST_print(BS);
	// Elemtype key;
	printf("please input search key: ");
	scanf("%d", &key);
	pos = BinarySearch(BS, key);
	if(pos != -1)
	{
		printf("find key, pos is %d.\n", pos);
	}
	else
	{
		printf("not find.\n");
	}
	return 0;
}

//  2024.06.25 学了c语言的部分内容，看到视频的13.4，明天继续吧。 21：52