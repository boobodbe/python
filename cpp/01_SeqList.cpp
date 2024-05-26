# include <stdio.h>
# include <stdlib.h>  // 包含malloc和free函数
# define ElemType int
# define MaxSize 10
# define InitSize 10
/*
 * 线性表的基本操作
 * InitList(&L):初始化表。构造一个空的线性表，分配内存空间
 * DestroyList(&L):销毁操作。销毁线性表，并释放线性表L所占用的内存空间
 * ListInsert(&L,i,e):插入操作。在表中的第i个位置插入指定元素e
 * ListDelete(&L,i, e):删除操作。删除表L中第i个位置上的元素，并用e返回删除元素的值
 * LocateElem(L, e):按值查找操作。在表中查找具有给定关键字值的元素
 * GetElem(L, i):按位查找操作。获取表L中第i个位置的元素的值
 * Length(L):求表长。返回线性表L的长度，即L中数据元素的个数
 * PrintList(L):输出操作。按前后顺序输出线性表L的所有元素值
 * Empty(L):判空操作。若L为空表，则返回true,否则返回false 
 *
 * 顺序表的特点
 * 1. 随机访问，即可以在O(1)的时间内找到第i个元素
 * 2. 存储密度高，每个节点只存储数据元素
 * 3. 拓展容量不方便（即便采用动态分配的方式实现，拓展长度的时间复杂度也比较高
 * 4. 插入、删除操作不方便，需要移动大量元素
*/

typedef struct{
	// 静态数组作为线性表的基本结构
	ElemType data[MaxSize];
	int length;
}SqList;

void InitList(SqList &L){
	// 初始化线性表，并把所有位置都设为0
	for(int i = 0; i < MaxSize; i++)
		L.data[i] = 0;
	L.length = 0;
}

void print_SqList(SqList L){
	// 打印输出整个线性表
	for(int i = 0; i < MaxSize; i++)
		printf("data[%d] = %d\n", i, L.data[i]);
}

void ListInsert(SqList &L, int i, int e){
	// 用静态分配实现顺序表的插入
	if(i >= 1 && i <= L.length){
		for(int j = L.length; j >= i; j--)
			L.data[j] = L.data[j-1];
		L.data[i-1] = e;
		L.length++;
	}else{
		printf("out of range.\n");
	}
}

void ListDel(SqList &L, int i, int &e){
	// 顺序表的删除操作
	if(i >= 1 && i <= L.length){
		e = L.data[i-1];
		for(int j = i; j < L.length; j++)  // 这里写错了，原来写的是j--，一直运行不成功，要注意细节
			L.data[j-1] = L.data[j];
		L.length--;
	}else{
		printf("out of range.\n");
	}
}

void LocateElem(SqList L, int e){
	// 按值查找
	int i;
	for(i = 0; i < L.length; i++){
		if(L.data[i] == e){
			printf("%d 在顺序表中的位置是：%d.\n", e, i+1);
			break;
		}
	}
	if(i == L.length)
		printf("在线性表中未找到%d。\n", e);
}

void GetElem(SqList L, int i){
	// 按位查找
	if(i < 1 || i > L.length){
		printf("out of range");
	}else if(i >= 1 && i <= L.length){
		printf("第%d个元素是%d.\n", i, L.data[i-1]);
	}else{
		printf("没找到。\n");
	}
}

// 以上是静态数组，以下是动态数组

typedef struct{
	// 动态分配实现
	int *data;
	int MaxSeqSize;
	int length;
}SeqList;

void InitSeqList(SeqList &L){
	// 用malloc函数申请一片空间
	L.data = (int *)malloc(sizeof(int) * InitSize);
	L.length = 0;
	L.MaxSeqSize = InitSize;
}

void IncreaseSize(SeqList &L, int len){
	// 增加动态数组的长度
	int *p = L.data;
	L.data = (int *)malloc((L.MaxSeqSize + len) * sizeof(int));
	for(int i = 0; i < L.length; i++)
		L.data[i] = p[i];  // 将数据复制到新的区域
	L.MaxSeqSize = L.MaxSeqSize + len;
	free(p);  // 释放原来的内存空间
}

void print_SeqList(SeqList L){
	// 打印输出整个动态线性表
	for(int i = 0; i < L.length; i++)
		printf("data[%d] = %d\n", i, L.data[i]);
}

// c -- malloc、free函数
// L.data = (ElemType *)malloc(sizeof(ElemType)*InitSize);

int main(){
	printf("Hello World!\n");
	// 静态线性表，不可扩容的
	SqList L;
	InitList(L);
	for(int i = 0; i < 4; i++){
		L.data[i] = i+1;
		L.length++;
	}
	int k =-1;
	ListInsert(L, 3, 22);
	ListDel(L, 6, k);
	printf("the del num is %d.\n", k);
	print_SqList(L);
	printf("The length of L is %d.\n", L.length);
	LocateElem(L, 4);
	GetElem(L, 6);

	// 动态线性表，可以扩容
	SeqList LL;
	InitSeqList(LL);
	for(int i = 0; i < LL.MaxSeqSize; i++){
		LL.data[i] = i;
		LL.length++;
	}
	IncreaseSize(LL, 5);
	LL.data[10] = 11;
	LL.length++;
	// printf("The length of LL is %d.\n", LL.length);
	// printf("The MaxSeqSize of LL is %d.\n", LL.MaxSeqSize);
	// print_SeqList(LL);
	return 0;
}