// 王道的题：http://oj.lgwenda.com/problem/16

#include <stdio.h>

typedef struct
{
	int data[50];
	int length;
}SqList;

void print(SqList L)
{
	for(int i = 0; i<L.length; i++)
	{
		printf("%3d", L.data[i]);
	}
	printf("\n");
}

void ListInsert(SqList &L, int elem)
{
	for(int j = L.length; j > 1; j--)
	{
		L.data[j] = L.data[j-1];
	}
	L.data[1] = elem;
	L.length++;
}

bool DeleElem(SqList &L, int pos)
{
	if(pos<1 || pos > L.length)
	{
		return false;
	}
	for(int j = pos; j<L.length; j++)
	{
		L.data[j-1] = L.data[j];
	}
	L.length--;
	return true;
}

int main(int argc, char const *argv[])
{
	SqList L;
	L.data[0] = 1;
	L.data[1] = 2;
	L.data[2] = 3;
	L.length = 3;
	int num;
	scanf("%d", &num);
	ListInsert(L, num);
	print(L);
	int del;
	bool res;
	scanf("%d", &del);
	res = DeleElem(L, del);
	if(res)
	{
		print(L);
	}
	else
	{
		printf("false");
	}
	return 0;
}